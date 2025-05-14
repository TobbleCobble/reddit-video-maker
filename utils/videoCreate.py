from moviepy.editor import *
from moviepy.video import *
import moviepy.editor as mpe
import os
import random


def createVideo(username):
    audioClip = []
    imageClip = []
    length = -0.5

    startTimes = [0]

    if os.path.exists(username+"/constructed.mp4"):
        os.remove(username+"/constructed.mp4")

    for files in os.listdir("temp/"+username+""):
        if ".mp3" in files: 
            audioClip.append(AudioFileClip("temp/"+username+"/"+files).set_start(length+0.5))
            length += AudioFileClip("temp/"+username+"/"+files).duration + 0.5
            startTimes.append(length)
            
    i = 0
    for files in os.listdir("temp/"+username+""):

        if ".png" in files:
            clip = ImageClip("temp/"+username+"/"+files,duration=audioClip[i].duration).set_start(startTimes[i])
            
            (w,h) = clip.size
            clip = clip.resize(newsize=(w*1.3,h*1.3))
            (w,h) = (w*1.3,h*1.3)
            clip = clip.set_position((360-w/2,640-h/2))
            clip = clip.set_opacity(0.9)
            imageClip.append(clip)
            i += 1

    videoAudio = CompositeAudioClip(audioClip)

    backgroundClip = ColorClip((720,1280), (0,0,255), duration=videoAudio.duration)
    bg_file = os.listdir("assets/bg_vids")[random.randrange(0,len(os.listdir("assets/bg_vids")))]
    backgroundClip = VideoFileClip("assets/bg_vids/"+bg_file)
    if int(backgroundClip.duration-videoAudio.duration) <= 0:
        repeats = int(videoAudio.duration/backgroundClip.duration) + 1
        repeated_clips = [backgroundClip] * repeats
        backgroundClip = concatenate_videoclips(repeated_clips, method="compose")
    videoStart = max(int(backgroundClip.duration-videoAudio.duration), 0)
    videoStart = random.randrange(0,videoStart)
    backgroundClip = backgroundClip.subclip(videoStart, videoStart + videoAudio.duration)
    
    videoClip = backgroundClip
    videoClip = CompositeVideoClip([videoClip] + imageClip)
    audio_background = mpe.AudioFileClip("assets/music/"+os.listdir("assets/music")[random.randrange(0,len(os.listdir("assets/music")))])
    final_audio = mpe.CompositeAudioClip([videoAudio, audio_background]).set_duration(backgroundClip.duration)
    videoClip.audio = final_audio
    videoClip.write_videofile("exports/"+username+".mp4", fps=30)

if __name__ == "__main__":
    createVideo("post")
