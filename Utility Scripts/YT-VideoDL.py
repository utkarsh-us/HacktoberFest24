import youtube_dl

def download_video(url, output_path='downloads', format='bestaudio/best'):
    options = {
        'format': format,
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = info_dict.get('title', None)
        
        if video_title:
            print(f'Downloaded: {video_title}')
        else:
            print('Download failed. Check the provided URL.')

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
