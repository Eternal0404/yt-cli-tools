"""
Unit tests for downloader module.
"""

import unittest
from unittest.mock import patch, MagicMock
from yt_cli.downloader import download_progress_hook


class TestDownloader(unittest.TestCase):
    """Test cases for downloader functionality."""
    
    def test_download_progress_hook_downloading(self):
        """Test progress hook during download."""
        d = {
            'status': 'downloading',
            '_percent_str': '50%',
            '_speed_str': '1MB/s',
            '_eta_str': '00:30'
        }
        # Should not raise an error
        download_progress_hook(d)
    
    def test_download_progress_hook_finished(self):
        """Test progress hook when download finished."""
        d = {
            'status': 'finished'
        }
        # Should not raise an error
        download_progress_hook(d)
    
    @patch('yt_cli.downloader.validate_youtube_url')
    def test_download_video_invalid_url(self, mock_validate):
        """Test download with invalid URL."""
        mock_validate.return_value = False
        
        from yt_cli.downloader import download_video
        with self.assertRaises(SystemExit):
            download_video("invalid_url")


if __name__ == '__main__':
    unittest.main()
