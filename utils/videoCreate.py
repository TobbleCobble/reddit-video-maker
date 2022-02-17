from moviepy.editor import *
from moviepy.video import *
import os


def createVideo(post):
    audioClip = []
    imageClip = []
    length = -0.5

    startTimes = [0]

    if os.path.exists("temp/constructed.mp4"):
        os.remove("temp/constructed.mp4")
    

    for files in os.listdir("temp"):
        if ".mp3" in files: 
            audioClip.append(AudioFileClip("temp/"+files).set_start(length+0.5))
            length += AudioFileClip("temp/"+files).duration + 0.5
            startTimes.append(length)
    print(startTimes)
    i = 0
    for files in os.listdir("temp"):

        if ".png" in files:
            clip = ImageClip("temp/"+files,duration=audioClip[i].duration).set_start(startTimes[i])
            
            (w,h) = clip.size
            clip = clip.resize(newsize=(w*1.3,h*1.3))
            (w,h) = (w*1.3,h*1.3)
            clip = clip.set_position((360-w/2,640-h/2))
            imageClip.append(clip)
            i += 1
    i = 0

    #videoImages = CompositeVideoClip(imageClip)
    videoAudio = CompositeAudioClip(audioClip)

    #(w, h) = videoImages.size

    #videoImages.crop(width=720,height=1280, x_center=w/2, y_center=h/2)
    
    videoClip = ColorClip((720,1280), (0,0,255), duration=videoAudio.duration)
    videoClip = CompositeVideoClip([videoClip] + imageClip)
    videoClip.audio = videoAudio
    videoClip.write_videofile("temp/constructed.mp4", fps=30)

    for files in os.listdir("temp"):
        if ".mp3" in files or ".png" in files: 
            os.remove("temp/"+files)

if __name__ == "__main__":
    createVideo("post")
