from moviepy.editor import *
from moviepy.video import *
import moviepy.editor as mpe
import os
import random
import time


def createVideo(username):
    audioClip = []
    imageClip = []
    length = -0.5

    startTimes = [0]

    if os.path.exists(username+"/constructed.mp4"):
        os.remove(username+"/constructed.mp4")
    

    for files in os.listdir(username+""):
        if ".mp3" in files: 
            audioClip.append(AudioFileClip(username+"/"+files).set_start(length+0.5))
            length += AudioFileClip(username+"/"+files).duration + 0.5
            startTimes.append(length)
            
    i = 0
    for files in os.listdir(username+""):

        if ".png" in files:
            clip = ImageClip(username+"/"+files,duration=audioClip[i].duration).set_start(startTimes[i])
            
            (w,h) = clip.size
            clip = clip.resize(newsize=(w*1.3,h*1.3))
            (w,h) = (w*1.3,h*1.3)
            clip = clip.set_position((360-w/2,640-h/2))
            clip = clip.set_opacity(0.9)
            imageClip.append(clip)
            i += 1
    i = 0

    #videoImages = CompositeVideoClip(imageClip)
    videoAudio = CompositeAudioClip(audioClip)

    backgroundClip = ColorClip((720,1280), (0,0,255), duration=videoAudio.duration)
    bg_file = os.listdir("assets/bg_vids")[random.randrange(0,len(os.listdir("assets/bg_vids")))]
    backgroundClip = VideoFileClip("assets/bg_vids/"+bg_file)
    videoStart = int(backgroundClip.duration-videoAudio.duration)
    videoStart = random.randrange(0,videoStart)
    backgroundClip = backgroundClip.subclip(videoStart, videoStart + videoAudio.duration)
    print(bg_file)
    #(w, h) = videoImages.size

    #videoImages.crop(width=720,height=1280, x_center=w/2, y_center=h/2)
    
    videoClip = backgroundClip
    videoClip = CompositeVideoClip([videoClip] + imageClip)
    audio_background = mpe.AudioFileClip("assets/music/"+os.listdir("assets/music")[random.randrange(0,len(os.listdir("assets/music")))])
    final_audio = mpe.CompositeAudioClip([videoAudio, audio_background]).set_duration(backgroundClip.duration)
    videoClip.audio = final_audio
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
