# Simple script to download playlist from youtube via pytube api
# This file tested with python3.7
# To install the package pytube: pip3.7 install pytube
# Made by Ahmed Darbi <https://www.linkedin.com/in/ahmed-darbi/>


# Import lib
import re
from pytube import Playlist

# Download folder
DOWNLOAD_DIR = 'C:\\Mastering_Python'

# To be change (Playlist)
playlist = Playlist('https://www.youtube.com/playlist?list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs')

# This fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

# Browse/download links
for video in playlist.videos:
    stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    try:
        # Downloaded the links
        stream.download(output_path=DOWNLOAD_DIR)
    except:
        # Print exception link
        print('Some error in downloading: ', video.embed_url)
