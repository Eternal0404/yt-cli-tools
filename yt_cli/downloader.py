"""
YouTube video and audio downloader module.
"""

import sys
import os
from pathlib import Path
from typing import Optional
import yt_dlp
from .utils import print_error, print_success, print_info, validate_youtube_url


def download_video(video_url: str, audio_only: bool = False, output_path: str = ".") -> None:
    """
    Download YouTube video or audio.
    
    Args:
        video_url: YouTube video URL
        audio_only: If True, download audio only
        output_path: Directory to save the download
    """
    if not validate_youtube_url(video_url):
        print_error("Invalid YouTube URL")
        sys.exit(1)
    
    # Ensure output directory exists
    Path(output_path).mkdir(parents=True, exist_ok=True)
    
    # Configure download options
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
        'progress_hooks': [download_progress_hook],
    }
    
    if audio_only:
        print_info("Downloading audio only...")
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        print_info("Downloading video...")
        ydl_opts.update({
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        })
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            print_info(f"Title: {info.get('title', 'Unknown')}")
            print_info(f"Duration: {info.get('duration', 0)} seconds")
            
            ydl.download([video_url])
            
        file_type = "audio" if audio_only else "video"
        print_success(f"Successfully downloaded {file_type} to {output_path}")
        
    except yt_dlp.utils.DownloadError as e:
        print_error(f"Download failed: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print_error(f"An error occurred: {str(e)}")
        sys.exit(1)


def download_progress_hook(d):
    """Hook function to display download progress."""
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"\rDownloading: {percent} at {speed} ETA: {eta}", end='', flush=True)
    elif d['status'] == 'finished':
        print("\n", end='')
        print_info("Download completed, processing...")
