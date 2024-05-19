from pytube import YouTube

try:
    url = input("Enter the YouTube URL: ")
    
    yt = YouTube(url)
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    video = yt.streams.get_highest_resolution()
    loc = input("Enter your location for download")    
    video.download(loc)
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))