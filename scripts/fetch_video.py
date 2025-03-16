import os
from typing import NoReturn
import yt_dlp

def download_youtube_video(video_url: str, output_folder: str = "video") -> NoReturn:
    """
    Download a YouTube video to a specified folder using yt-dlp.
    
    :param video_url: The URL of the YouTube video to download
    :param output_folder: The folder where the downloaded file should be saved (defaults to 'video')
    """
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder, exist_ok=True)
    
    # Configure yt-dlp options
    ydl_opts = {
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'format': 'mp4/bestaudio/best',
    }
    
    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print(f"Download completed. Saved to '{output_folder}'")

if __name__ == "__main__":
    youtube_url: str = "https://www.youtube.com/watch?v=ukmu4DPgtOo&t=249s"
    download_youtube_video(youtube_url)
