from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("There has been an error")
        print("Download is complete!!! Enjoy!")
        
    link = input("Enter YouTube link...!! URL: ")
    Download(link)
    