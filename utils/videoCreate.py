from moviepy.editor import *
from moviepy.video import *
import os


def createVideo(post):
    audioClip = []
    length = -0.5

    if os.path.exists("temp/constructed.mp4"):
        os.remove("temp/constructed.mp4")

    for files in os.listdir("temp"):
        audioClip.append(AudioFileClip("temp/"+files).set_start(length+0.5))
        length += AudioFileClip("temp/"+files).duration + 0.5

    videoAudio = CompositeAudioClip(audioClip)
    
    videoClip = ColorClip((720,1280), (0,0,0), duration=videoAudio.duration)
    videoClip.audio = videoAudio
    videoClip.write_videofile("temp/constructed.mp4", fps=30)

createVideo("post")
