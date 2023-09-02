from pytube import YouTube

def on_download_progress(stream,chunk,bytes_remaining):
        bytes_download = stream.filesize - bytes_remaining
        percent = bytes_download * 100 / stream.filesize
        print(f"progression du telechargement : {int(percent)}%")


while True:

    try:
        url = input("Antre yon lyen YouTube: ")
        youtube_video = YouTube(url)
        break
    except Exception as e:
        print(f"gen yon ere:{e}")

if youtube_video:        

    youtube_video.register_on_progress_callback(on_download_progress)

    print("titre:"+ youtube_video.title)
    print("NB VUES :",youtube_video.views)

    print("STREAMS")
    for stream in youtube_video.streams.fmt_streams:
        print(" ",stream)

    stream = youtube_video.streams.get_highest_resolution()
    print("stream video",stream)
    print("downloading...")
    stream.download()  
    print("Done")  
else:
    print("pwogram nan ap kontinye...")    

