"""
YouTube video metadata extraction module.
"""

import sys
import json
from typing import Dict, Any
import yt_dlp
from .utils import print_error, print_success, print_info, validate_youtube_url, format_duration


def extract_metadata(video_url: str, output_json: bool = False) -> None:
    """
    Extract and display metadata from a YouTube video.
    
    Args:
        video_url: YouTube video URL
        output_json: If True, output as JSON
    """
    if not validate_youtube_url(video_url):
        print_error("Invalid YouTube URL")
        sys.exit(1)
    
    print_info("Extracting metadata...")
    
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'extract_flat': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            
            # Extract relevant metadata
            metadata = {
                'title': info.get('title', 'N/A'),
                'channel': info.get('uploader', 'N/A'),
                'channel_id': info.get('channel_id', 'N/A'),
                'duration': info.get('duration', 0),
                'duration_formatted': format_duration(info.get('duration', 0)),
                'view_count': info.get('view_count', 0),
                'like_count': info.get('like_count', 0),
                'upload_date': info.get('upload_date', 'N/A'),
                'description': info.get('description', 'N/A'),
                'thumbnail': info.get('thumbnail', 'N/A'),
                'video_id': info.get('id', 'N/A'),
                'url': video_url,
                'categories': info.get('categories', []),
                'tags': info.get('tags', []),
            }
            
            if output_json:
                # Output as JSON
                print(json.dumps(metadata, indent=2))
            else:
                # Output as formatted text
                print_success("Metadata extracted:\n")
                print("=" * 80)
                print(f"Title:        {metadata['title']}")
                print(f"Channel:      {metadata['channel']}")
                print(f"Video ID:     {metadata['video_id']}")
                print(f"Duration:     {metadata['duration_formatted']}")
                print(f"Views:        {metadata['view_count']:,}")
                print(f"Likes:        {metadata['like_count']:,}")
                print(f"Upload Date:  {metadata['upload_date']}")
                print(f"Thumbnail:    {metadata['thumbnail']}")
                
                if metadata['categories']:
                    print(f"Categories:   {', '.join(metadata['categories'])}")
                
                if metadata['tags']:
                    tags_preview = ', '.join(metadata['tags'][:5])
                    if len(metadata['tags']) > 5:
                        tags_preview += f"... (+{len(metadata['tags']) - 5} more)"
                    print(f"Tags:         {tags_preview}")
                
                print(f"\nDescription:")
                print("-" * 80)
                # Limit description to first 500 characters
                desc = metadata['description']
                if len(desc) > 500:
                    desc = desc[:500] + "..."
                print(desc)
                print("=" * 80)
            
    except yt_dlp.utils.DownloadError as e:
        print_error(f"Failed to extract metadata: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print_error(f"An error occurred: {str(e)}")
        sys.exit(1)
