"""
Transcript fetching and summarization module.
"""

import sys
from typing import Optional
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from .utils import print_error, print_success, print_info, extract_video_id


def fetch_transcript(video_url: str) -> Optional[str]:
    """
    Fetch transcript from a YouTube video.
    
    Args:
        video_url: YouTube video URL
        
    Returns:
        Full transcript text or None if unavailable
    """
    video_id = extract_video_id(video_url)
    if not video_id:
        print_error("Invalid YouTube URL")
        return None
    
    try:
        print_info(f"Fetching transcript for video ID: {video_id}")
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Combine all transcript segments
        full_transcript = " ".join([entry['text'] for entry in transcript_list])
        return full_transcript
        
    except TranscriptsDisabled:
        print_error("Transcripts are disabled for this video")
        return None
    except NoTranscriptFound:
        print_error("No transcript found for this video")
        return None
    except Exception as e:
        print_error(f"Failed to fetch transcript: {str(e)}")
        return None


def summarize_text(text: str, summary_type: str = "medium") -> str:
    """
    Summarize text based on the summary type.
    
    Args:
        text: Text to summarize
        summary_type: Type of summary (short, medium, long)
        
    Returns:
        Summarized text
    """
    words = text.split()
    total_words = len(words)
    
    # Define summary lengths
    summary_lengths = {
        "short": min(100, total_words // 10),
        "medium": min(300, total_words // 4),
        "long": min(600, total_words // 2)
    }
    
    target_length = summary_lengths.get(summary_type, summary_lengths["medium"])
    
    # Simple extractive summary: take first N words
    # In production, you might want to use NLP libraries like NLTK or spaCy
    summary_words = words[:target_length]
    summary = " ".join(summary_words)
    
    # Add ellipsis if truncated
    if len(words) > target_length:
        summary += "..."
    
    return summary


def generate_summary(video_url: str, summary_type: str = "medium") -> None:
    """
    Generate and print a summary of a YouTube video transcript.
    
    Args:
        video_url: YouTube video URL
        summary_type: Type of summary (short, medium, long)
    """
    if summary_type not in ["short", "medium", "long"]:
        print_error(f"Invalid summary type: {summary_type}. Use 'short', 'medium', or 'long'")
        sys.exit(1)
    
    transcript = fetch_transcript(video_url)
    
    if transcript:
        print_info(f"Generating {summary_type} summary...")
        summary = summarize_text(transcript, summary_type)
        
        print_success("Summary generated:\n")
        print("=" * 80)
        print(summary)
        print("=" * 80)
        print(f"\nOriginal length: {len(transcript.split())} words")
        print(f"Summary length: {len(summary.split())} words")
    else:
        print_error("Could not generate summary")
        sys.exit(1)
