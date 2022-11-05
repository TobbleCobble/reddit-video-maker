from moviepy.editor import *
from moviepy.video import *
import os
import random
import time


def createVideo(username):
    audioClip = []
    imageClip = []
    length = 0.5

    startTimes = [0]

    #if os.path.exists("/exports/"+username+"/constructed.mp4"):
    #    os.remove(username+"/constructed.mp4")
    

    for files in os.listdir(username+""):
        if ".mp3" in files: 
            audioClip.append(AudioFileClip(username+"/"+files).set_start(length - 0.5))
            length += AudioFileClip(username+"/"+files).duration - 0.5
            startTimes.append(length - 0.5)
            
    i = 0
    for files in os.listdir(username+""):

        if ".png" in files:
            clip = ImageClip(username+"/"+files,duration=audioClip[i].duration - 0.5).set_start(startTimes[i])
            
            (w,h) = clip.size
            clip = clip.resize(newsize=(w*2,h*2))
            (w,h) = (w*2,h*2)
            clip = clip.set_position((540-w/2,960-h/2))
            clip = clip.set_opacity(0.9)
            imageClip.append(clip)
            i += 1
    i = 0

    #videoImages = CompositeVideoClip(imageClip)
    videoAudio = CompositeAudioClip(audioClip)

    backgroundClip = ColorClip((720,1280), (0,0,255), duration=videoAudio.duration)
    bg_file = os.listdir("bg_vids")[random.randrange(0,len(os.listdir("bg_vids")))]
    backgroundClip = VideoFileClip("bg_vids/"+bg_file)
    videoStart = int(backgroundClip.duration-videoAudio.duration)
    videoStart = random.randrange(0,videoStart)
    backgroundClip = backgroundClip.subclip(videoStart, videoStart + videoAudio.duration)
    print(bg_file)
    #(w, h) = videoImages.size

    #videoImages.crop(width=720,height=1280, x_center=w/2, y_center=h/2)
    
    videoClip = backgroundClip
    videoClip = CompositeVideoClip([videoClip] + imageClip)
    videoClip.audio = videoAudio
    videoClip.write_videofile("exports/"+username+".mp4", fps=30)

    time.sleep(5)

    

    '''while len(os.listdir(username+"")) > 0:
        for files in os.listdir(username+""):
            if ".mp3" in files or ".png" in files: 
                try:
                    os.remove(username+"/"+files)
                except:
                    continue'''

if __name__ == "__main__":
    createVideo("post")
