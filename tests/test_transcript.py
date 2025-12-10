"""
Unit tests for transcript module.
"""

import unittest
from unittest.mock import patch, MagicMock
from yt_cli.transcript import fetch_transcript, summarize_text


class TestTranscript(unittest.TestCase):
    """Test cases for transcript functionality."""
    
    def test_summarize_text_short(self):
        """Test short summary generation."""
        text = " ".join(["word"] * 1000)
        summary = summarize_text(text, "short")
        self.assertLessEqual(len(summary.split()), 100)
    
    def test_summarize_text_medium(self):
        """Test medium summary generation."""
        text = " ".join(["word"] * 1000)
        summary = summarize_text(text, "medium")
        self.assertLessEqual(len(summary.split()), 300)
    
    def test_summarize_text_long(self):
        """Test long summary generation."""
        text = " ".join(["word"] * 1000)
        summary = summarize_text(text, "long")
        self.assertLessEqual(len(summary.split()), 600)
    
    @patch('yt_cli.transcript.YouTubeTranscriptApi.get_transcript')
    @patch('yt_cli.transcript.extract_video_id')
    def test_fetch_transcript_success(self, mock_extract_id, mock_get_transcript):
        """Test successful transcript fetching."""
        mock_extract_id.return_value = "test_video_id"
        mock_get_transcript.return_value = [
            {'text': 'Hello', 'start': 0.0},
            {'text': 'World', 'start': 1.0}
        ]
        
        result = fetch_transcript("https://youtube.com/watch?v=test")
        self.assertEqual(result, "Hello World")
    
    @patch('yt_cli.transcript.extract_video_id')
    def test_fetch_transcript_invalid_url(self, mock_extract_id):
        """Test transcript fetching with invalid URL."""
        mock_extract_id.return_value = None
        
        result = fetch_transcript("invalid_url")
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
