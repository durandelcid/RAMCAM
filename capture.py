#Script to capture RAMCAM webcam
#Dependencies: (python-ffmpeg) & (ffmpeg) & (yt_dlp)

import ffmpeg #Imports using ffmpeg-python package

import yt_dlp #Relies on ffmpeg
from yt_dlp import YoutubeDL #Python class provided by yt-dlp library


#Potential useful options for yt_dlp
# --live-from-start
# -P "[PATH]"

#epoch: "Unix epoch of when the information extraction was completed"
#Or use the Python time function?

opts ={
        'format': 'bv', #Only record in best video quality (does not include audio)
        'postprocessors': [{ #This is what changes the file format from whatever it records in (I believe mp4 / WebM to mkv)
            'key': 'FFmpegVideoRemuxer',
            'preferedformat': 'mkv',
        }],
        'outtmpl': '%(epoch)d',  #What the filename will be
    }
ydl = YoutubeDL(opts) #Creating a yt_dlp object with options defined

ydl.download("https://www.youtube.com/watch?v=p-Bc_NiCh9A") #Downloading RAMCAM livestream

#Hello world comment from desktop