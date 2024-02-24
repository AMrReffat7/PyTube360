from pytube import YouTube

try:  
    link = input("      Enter the link").strip()
    video = YouTube(link)
except:
    print("Connection Error")

print("     Title",video.title)
print("     Views",video.views)
print("     Description",video.description)

videoDownload = video.streams.get_by_resolution(360)
videoDownload.download('C:\\Users\\RTX\\Downloads\\Video')
print("     Download completed successfully.")