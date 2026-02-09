## YT Downloader

A simple **YouTube video / audio downloader** desktop application.  
You can paste a video link and download it as **MP3** or **MP4**, and select resolution for MP4 downloads.

### Features
- **Simple UI**: Desktop app built with PyQt5  
- **Format selection**: MP3 (audio) or MP4 (video)  
- **Resolution selection**: For MP4, options from 1080p down to 144p  
- **Automatic naming**: Output file name based on the name you enter

### Requirements
- **Python 3.8+**
- These Python packages:
  - `yt_dlp`
  - `PyQt5`
  - **FFmpeg** installed on the system (required for MP3 conversion)

Install the Python dependencies with:

```bash
pip install yt-dlp PyQt5
```

If FFmpeg is not installed, download it for your OS and add it to your system `PATH`.

### How to Run
1. Download or clone this project to your computer.  
2. Go to the project directory:  

```bash
cd yt-downloader
```

3. Start the application:

```bash
python main.py
```

### Usage
- **Video link**: Paste the URL of the YouTube video you want to download.  
- **File name**: Enter the output file name (no need to write the extension).  
- **Select format**:
  - If you select `mp3`, only audio will be downloaded.
  - If you select `mp4`, video will be downloaded and the resolution dropdown will be shown.
- **Select resolation**: Choose the desired resolution for MP4 format.  
- Click **Download**:
  - Progress / result will be shown in the `Status` label.

### Notes
- For MP3 downloads, quality is set to `192 kbps` by default.  
- For MP4 downloads, the best available quality **not higher than** the selected resolution is used.  
- If you get errors:
  - Make sure the link is a valid YouTube URL.
  - Check your internet connection and FFmpeg installation.
