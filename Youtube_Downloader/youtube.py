import os
from pytube import YouTube

def download_video(url, file_type):
    try:
        yt = YouTube(url)
    except Exception as e:
        print(f"Error: {e}")
        return

    if file_type == 'mp3':
        try:
            stream = yt.streams.filter(only_audio=True).first()
            original_filename = stream.default_filename
            audio_path = os.path.join("MP3", os.path.splitext(original_filename)[0] + '.mp3')
            stream.download(output_path="MP3", filename=os.path.basename(audio_path))
            print(f"Downloaded successfully as {audio_path}")
        except Exception as e:
            print(f"MP3 download error: {e}") 

    elif file_type == 'mp4':
        try:
            stream = yt.streams.get_highest_resolution()  
            original_filename = stream.default_filename
            video_path = os.path.join("MP4", original_filename)
            stream.download(output_path="MP4", filename=os.path.basename(video_path))
            print(f"Downloaded successfully as {video_path}")
        except Exception as e:
            print(f"MP4 download error: {e}")

    else:
        print("Invalid file type. Please choose 'mp3' or 'mp4'.")

if __name__ == "__main__":
    if not os.path.exists("MP3"):
        os.makedirs("MP3")
    if not os.path.exists("MP4"):
        os.makedirs("MP4")

    while True:
        url = input("Enter the YouTube URL (or type 'q' to quit): ")
        if url.lower() == 'q':
            break

        file_type = input("Enter file type (mp3 or mp4): ").lower()
        if file_type in ['mp3', 'mp4']:
            download_video(url, file_type)
        else:
            print("Invalid file type.")
