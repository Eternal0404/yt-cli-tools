"""
Unit tests for converter module.
"""

import unittest
from unittest.mock import patch, MagicMock
from yt_cli.converter import check_ffmpeg


class TestConverter(unittest.TestCase):
    """Test cases for converter functionality."""
    
    @patch('subprocess.run')
    def test_check_ffmpeg_installed(self, mock_run):
        """Test FFmpeg detection when installed."""
        mock_run.return_value = MagicMock()
        result = check_ffmpeg()
        self.assertTrue(result)
    
    @patch('subprocess.run')
    def test_check_ffmpeg_not_installed(self, mock_run):
        """Test FFmpeg detection when not installed."""
        mock_run.side_effect = FileNotFoundError()
        result = check_ffmpeg()
        self.assertFalse(result)
    
    @patch('yt_cli.converter.check_ffmpeg')
    @patch('yt_cli.converter.Path')
    def test_convert_file_no_ffmpeg(self, mock_path, mock_check):
        """Test conversion without FFmpeg installed."""
        mock_check.return_value = False
        
        from yt_cli.converter import convert_file
        with self.assertRaises(SystemExit):
            convert_file("test.mp4", "mp3")


if __name__ == '__main__':
    unittest.main()
