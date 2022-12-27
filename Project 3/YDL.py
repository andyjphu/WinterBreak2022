import youtube_dl
def run(video_url):
    #video_url = input("please enter youtube video url:")
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))

if __name__=='__main__':
    run()
    
    
    #youtube-dl -i PLwJ2VKmefmxpUJEGB1ff6yUZ5Zd7Gegn2
    #youtube-dl -i --no-check-certificate -f bestaudio PL6PRFQKbF3ser6ymt0eiMtaktosaD_k5Y 