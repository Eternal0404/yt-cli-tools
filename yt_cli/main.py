"""
Main CLI entry point for YT CLI Tools.
"""

import argparse
import sys
from . import __version__
from .transcript import generate_summary
from .downloader import download_video
from .converter import convert_file, compress_file, compress_folder
from .metadata import extract_metadata
from .utils import print_error


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        prog='yt-cli',
        description='YT CLI Tools - A comprehensive toolkit for YouTube content creators',
        epilog='For more information, visit: https://github.com/YOUR_USERNAME/yt-cli-tools'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version=f'%(prog)s {__version__}'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Transcript command
    transcript_parser = subparsers.add_parser(
        'transcript',
        help='Fetch and summarize YouTube video transcript'
    )
    transcript_parser.add_argument(
        'url',
        help='YouTube video URL'
    )
    transcript_parser.add_argument(
        '--summary',
        choices=['short', 'medium', 'long'],
        default='medium',
        help='Summary length (default: medium)'
    )
    
    # Download command
    download_parser = subparsers.add_parser(
        'download',
        help='Download YouTube video or audio'
    )
    download_parser.add_argument(
        'url',
        help='YouTube video URL'
    )
    download_parser.add_argument(
        '--audio',
        action='store_true',
        help='Download audio only (MP3 format)'
    )
    download_parser.add_argument(
        '--output',
        '-o',
        default='.',
        help='Output directory (default: current directory)'
    )
    
    # Convert command
    convert_parser = subparsers.add_parser(
        'convert',
        help='Convert media file to a different format'
    )
    convert_parser.add_argument(
        'file',
        help='Input file path'
    )
    convert_parser.add_argument(
        '--to',
        required=True,
        help='Target format (e.g., mp3, mp4, avi)'
    )
    
    # Compress command
    compress_parser = subparsers.add_parser(
        'compress',
        help='Compress video file(s)'
    )
    compress_parser.add_argument(
        'path',
        help='File or folder path'
    )
    compress_parser.add_argument(
        '--quality',
        choices=['low', 'medium', 'high'],
        default='medium',
        help='Compression quality (default: medium)'
    )
    
    # Metadata command
    metadata_parser = subparsers.add_parser(
        'metadata',
        help='Extract YouTube video metadata'
    )
    metadata_parser.add_argument(
        'url',
        help='YouTube video URL'
    )
    metadata_parser.add_argument(
        '--json',
        action='store_true',
        help='Output as JSON'
    )
    
    return parser


def main():
    """Main CLI entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(0)
    
    try:
        if args.command == 'transcript':
            generate_summary(args.url, args.summary)
            
        elif args.command == 'download':
            download_video(args.url, args.audio, args.output)
            
        elif args.command == 'convert':
            convert_file(args.file, args.to)
            
        elif args.command == 'compress':
            import os
            if os.path.isdir(args.path):
                compress_folder(args.path, args.quality)
            else:
                compress_file(args.path, args.quality)
                
        elif args.command == 'metadata':
            extract_metadata(args.url, args.json)
            
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(130)
    except Exception as e:
        print_error(f"Unexpected error: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main()
