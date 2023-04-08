from pytube import YouTube
from moviepy.editor import *

# Prompt user for YouTube video URL
url = input("Enter YouTube video URL: ")

# Download the video
yt = YouTube(url)
yt_stream = yt.streams.filter(only_audio=True).first()
yt_stream.download()

# Convert the video to MP3
video_file = yt.title + '.mp4'
audio_file = yt.title + '.mp3'
video_clip = VideoFileClip(video_file)
audio_clip = video_clip.audio
audio_clip.write_audiofile(audio_file)

# Clean up the temporary video file
video_clip.close()
audio_clip.close()
os.remove(video_file)

print(f"Video '{yt.title}' has been converted to MP3!")
