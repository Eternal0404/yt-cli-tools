# YT CLI Tools

YT CLI tools: download YouTube videos/audio, generate transcript summaries, convert/compress media, and extract metadata — all from your terminal.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

## Features

- 📝 **Transcript Summarizer** - Fetch YouTube video transcripts and generate short, medium, or long summaries
- 📥 **Video/Audio Downloader** - Download YouTube videos or audio-only files in MP3 format
- 🔄 **Media Converter** - Convert media files between different formats (MP4, MP3, AVI, etc.)
- 🗜️ **Video Compressor** - Compress video files or entire folders with customizable quality settings
- 📊 **Metadata Extractor** - Extract detailed information about YouTube videos including title, duration, views, and more

## Requirements

- Python 3.7 or higher
- FFmpeg (required for download, convert, and compress features)

### Installing FFmpeg

**Windows:**
- Download from [ffmpeg.org](https://ffmpeg.org/download.html)
- Add FFmpeg to your system PATH

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt update
sudo apt install ffmpeg
```

## Installation

### From Source

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/yt-cli-tools.git
cd yt-cli-tools
```

2. Install the package:
```bash
pip install .
```

Or install in development mode:
```bash
pip install -e .
```

### Using pip (after publishing to PyPI)

```bash
pip install yt-cli-tools
```

## Usage

After installation, the `yt-cli` command will be available globally.

### Transcript Summarizer

Fetch and summarize YouTube video transcripts:

```bash
# Generate a medium-length summary (default)
yt-cli transcript https://youtu.be/VIDEO_ID

# Generate a short summary
yt-cli transcript https://youtu.be/VIDEO_ID --summary short

# Generate a long summary
yt-cli transcript https://youtu.be/VIDEO_ID --summary long
```

### Video/Audio Downloader

Download YouTube videos or audio:

```bash
# Download video
yt-cli download https://youtu.be/VIDEO_ID

# Download audio only (MP3)
yt-cli download https://youtu.be/VIDEO_ID --audio

# Download to specific directory
yt-cli download https://youtu.be/VIDEO_ID --output ./downloads
```

### Media Converter

Convert media files to different formats:

```bash
# Convert MP4 to MP3
yt-cli convert video.mp4 --to mp3

# Convert to AVI
yt-cli convert video.mp4 --to avi

# Convert to other formats
yt-cli convert input.mov --to mp4
```

### Video Compressor

Compress video files to reduce file size:

```bash
# Compress a single file (medium quality, default)
yt-cli compress video.mp4

# Compress with high quality (less compression)
yt-cli compress video.mp4 --quality high

# Compress with low quality (more compression)
yt-cli compress video.mp4 --quality low

# Compress all videos in a folder
yt-cli compress ./videos
```

### Metadata Extractor

Extract detailed metadata from YouTube videos:

```bash
# Display metadata in readable format
yt-cli metadata https://youtu.be/VIDEO_ID

# Output as JSON
yt-cli metadata https://youtu.be/VIDEO_ID --json
```

## Command Reference

```bash
yt-cli --help                    # Show help message
yt-cli --version                 # Show version

yt-cli transcript URL [--summary TYPE]
yt-cli download URL [--audio] [--output DIR]
yt-cli convert FILE --to FORMAT
yt-cli compress PATH [--quality LEVEL]
yt-cli metadata URL [--json]
```

## Examples

### Example 1: Download and Convert

Download a video and convert it to MP3:

```bash
yt-cli download https://youtu.be/VIDEO_ID
yt-cli convert "Video Title.mp4" --to mp3
```

### Example 2: Batch Compress Videos

Compress all videos in a folder:

```bash
yt-cli compress ./my_videos --quality medium
```

### Example 3: Get Video Info Before Downloading

Check metadata before downloading:

```bash
yt-cli metadata https://youtu.be/VIDEO_ID
yt-cli download https://youtu.be/VIDEO_ID --audio
```

## Development

### Running Tests

```bash
python -m pytest tests/
```

Or using unittest:

```bash
python -m unittest discover tests
```

### Project Structure

```
yt-cli-tools/
│
├── yt_cli/
│   ├── __init__.py          # Package initialization
│   ├── main.py              # CLI entry point and argument parsing
│   ├── downloader.py        # YouTube video/audio downloader
│   ├── transcript.py        # Transcript fetching and summarization
│   ├── converter.py         # Media format converter
│   ├── metadata.py          # YouTube metadata extractor
│   └── utils.py             # Utility functions
│
├── tests/
│   ├── __init__.py
│   ├── test_downloader.py
│   ├── test_transcript.py
│   └── test_converter.py
│
├── requirements.txt         # Project dependencies
├── setup.py                 # Package setup configuration
├── README.md               # Project documentation
├── LICENSE                 # MIT License
└── .gitignore             # Git ignore rules
```

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines

- Write clear, commented code
- Include unit tests for new features
- Update documentation as needed
- Follow PEP 8 style guidelines
- Ensure all tests pass before submitting

## Future Roadmap

- [ ] Add playlist download support
- [ ] Implement advanced NLP-based summarization using transformers
- [ ] Add subtitle download and translation features
- [ ] Support for multiple video platforms (Vimeo, Dailymotion, etc.)
- [ ] GUI version using tkinter or PyQt
- [ ] Batch processing with progress bars
- [ ] Video trimming and editing features
- [ ] Cloud storage integration (Google Drive, Dropbox)
- [ ] Docker containerization
- [ ] Web interface version

## Known Limitations

- Transcript feature only works for videos with available captions
- Download feature respects YouTube's terms of service (educational/personal use only)
- Compression and conversion quality depends on FFmpeg installation
- Some features may be region-restricted based on video availability

## Legal Notice

This tool is intended for personal and educational use only. Users are responsible for complying with YouTube's Terms of Service and copyright laws. Do not use this tool to download or distribute copyrighted content without permission.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube video downloader
- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) - Transcript fetching
- [FFmpeg](https://ffmpeg.org/) - Media processing

## Support

If you encounter any issues or have questions:

- Open an issue on [GitHub](https://github.com/YOUR_USERNAME/yt-cli-tools/issues)
- Check existing issues for solutions
- Provide detailed error messages and system information when reporting bugs

## Author

**Your Name**
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- Email: your.email@example.com

---

Made with ❤️ for content creators and video enthusiasts
