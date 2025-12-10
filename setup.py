"""
Setup script for YT CLI Tools.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read requirements
requirements = (this_directory / "requirements.txt").read_text(encoding='utf-8').splitlines()

setup(
    name='yt-cli-tools',
    version='1.0.0',
    author='Eternal0404',
    author_email='raiyanethar@gmail.com',
    description='YT CLI tools: download YouTube videos/audio, generate transcript summaries, convert/compress media, and extract metadata — all from your terminal.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/YOUR_USERNAME/yt-cli-tools',
    packages=find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Multimedia :: Video',
        'Topic :: Utilities',
    ],
    python_requires='>=3.7',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'yt-cli=yt_cli.main:main',
        ],
    },
    keywords='youtube video audio download transcript converter compressor cli',
    project_urls={
        'Bug Reports': 'https://github.com/YOUR_USERNAME/yt-cli-tools/issues',
        'Source': 'https://github.com/YOUR_USERNAME/yt-cli-tools',
    },
)
