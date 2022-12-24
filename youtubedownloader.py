import pytube

# Find the YouTube video URL
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Create a YouTube object
yt = pytube.YouTube(url)

# Get the first video stream available
stream = yt.streams.first()

# Download the video to the current working directory
stream.download()
