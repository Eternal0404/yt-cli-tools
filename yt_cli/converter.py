"""
Media converter and compressor module.
"""

import sys
import os
from pathlib import Path
from typing import List
import subprocess
from .utils import print_error, print_success, print_info, format_file_size


def check_ffmpeg() -> bool:
    """
    Check if FFmpeg is installed.
    
    Returns:
        True if FFmpeg is available, False otherwise
    """
    try:
        subprocess.run(['ffmpeg', '-version'], 
                      stdout=subprocess.PIPE, 
                      stderr=subprocess.PIPE,
                      check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def convert_file(input_file: str, output_format: str) -> None:
    """
    Convert media file to a different format.
    
    Args:
        input_file: Path to input file
        output_format: Target format (e.g., 'mp3', 'mp4', 'avi')
    """
    if not check_ffmpeg():
        print_error("FFmpeg is not installed. Please install FFmpeg to use this feature.")
        print_info("Download from: https://ffmpeg.org/download.html")
        sys.exit(1)
    
    input_path = Path(input_file)
    
    if not input_path.exists():
        print_error(f"File not found: {input_file}")
        sys.exit(1)
    
    # Create output filename
    output_file = input_path.with_suffix(f'.{output_format}')
    
    print_info(f"Converting {input_path.name} to {output_format}...")
    
    try:
        # Basic conversion command
        cmd = [
            'ffmpeg',
            '-i', str(input_path),
            '-y',  # Overwrite output file if exists
            str(output_file)
        ]
        
        result = subprocess.run(cmd, 
                              capture_output=True, 
                              text=True,
                              check=True)
        
        print_success(f"Converted to {output_file}")
        
        # Show file sizes
        original_size = input_path.stat().st_size
        new_size = output_file.stat().st_size
        print_info(f"Original: {format_file_size(original_size)}")
        print_info(f"Converted: {format_file_size(new_size)}")
        
    except subprocess.CalledProcessError as e:
        print_error(f"Conversion failed: {e.stderr}")
        sys.exit(1)
    except Exception as e:
        print_error(f"An error occurred: {str(e)}")
        sys.exit(1)


def compress_file(input_file: str, quality: str = "medium") -> None:
    """
    Compress a video file.
    
    Args:
        input_file: Path to input video file
        quality: Compression quality (low, medium, high)
    """
    if not check_ffmpeg():
        print_error("FFmpeg is not installed. Please install FFmpeg to use this feature.")
        print_info("Download from: https://ffmpeg.org/download.html")
        sys.exit(1)
    
    input_path = Path(input_file)
    
    if not input_path.exists():
        print_error(f"File not found: {input_file}")
        sys.exit(1)
    
    # Create output filename
    output_file = input_path.with_stem(f"{input_path.stem}_compressed")
    
    # CRF values (lower = better quality, larger file)
    crf_values = {
        "low": "28",      # More compression, lower quality
        "medium": "23",   # Balanced
        "high": "18"      # Less compression, higher quality
    }
    
    crf = crf_values.get(quality, "23")
    
    print_info(f"Compressing {input_path.name} (quality: {quality})...")
    
    try:
        cmd = [
            'ffmpeg',
            '-i', str(input_path),
            '-vcodec', 'libx264',
            '-crf', crf,
            '-preset', 'medium',
            '-y',
            str(output_file)
        ]
        
        result = subprocess.run(cmd,
                              capture_output=True,
                              text=True,
                              check=True)
        
        print_success(f"Compressed to {output_file}")
        
        # Show file sizes
        original_size = input_path.stat().st_size
        new_size = output_file.stat().st_size
        reduction = ((original_size - new_size) / original_size) * 100
        
        print_info(f"Original: {format_file_size(original_size)}")
        print_info(f"Compressed: {format_file_size(new_size)}")
        print_info(f"Size reduction: {reduction:.1f}%")
        
    except subprocess.CalledProcessError as e:
        print_error(f"Compression failed: {e.stderr}")
        sys.exit(1)
    except Exception as e:
        print_error(f"An error occurred: {str(e)}")
        sys.exit(1)


def compress_folder(folder_path: str, quality: str = "medium") -> None:
    """
    Compress all video files in a folder.
    
    Args:
        folder_path: Path to folder containing videos
        quality: Compression quality (low, medium, high)
    """
    folder = Path(folder_path)
    
    if not folder.exists() or not folder.is_dir():
        print_error(f"Folder not found: {folder_path}")
        sys.exit(1)
    
    # Find all video files
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv']
    video_files = []
    
    for ext in video_extensions:
        video_files.extend(folder.glob(f"*{ext}"))
    
    if not video_files:
        print_error(f"No video files found in {folder_path}")
        sys.exit(1)
    
    print_info(f"Found {len(video_files)} video file(s)")
    
    for video_file in video_files:
        print(f"\n{'=' * 80}")
        compress_file(str(video_file), quality)
    
    print(f"\n{'=' * 80}")
    print_success(f"Compressed {len(video_files)} video file(s)")
