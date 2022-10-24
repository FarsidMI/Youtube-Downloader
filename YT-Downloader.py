from pytube import YouTube

link = input("link: ")
yt = YouTube(link)

video = yt.streams.get_highest_resolution()
print("Title:", yt.title)
print("Views:", yt.views)

video.download()

print("Download Complete.")
