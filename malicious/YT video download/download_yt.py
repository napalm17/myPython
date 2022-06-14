import pytube

url = 'https://www.youtube.com/watch?v=qh4gNMB6QCQ&ab_channel=FeetLovers'

video = pytube.YouTube(url)

for stream in video.streams:
    print(stream)

stream = video.streams.get_by_itag(22)
stream.download(filename="vid")
print("done")