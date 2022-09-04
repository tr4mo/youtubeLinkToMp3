from pytube import YouTube
import os

#test link: OneRepublic - Sunshine (Official Audio)
#link = "https://www.youtube.com/watch?v=Jbch_x5132o"

def downloadSong(text):

    link = str(text)

    print(link)
    yt = YouTube(link)

    print("processing ...")

    video = yt.streams.filter(only_audio=True).first()

    print("downloading ...")

    out_file = video.download()

    base,ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)

    return yt.title