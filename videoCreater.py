from moviepy.editor import *
from moviepy.video import *
from moviepy.video.fx.all import crop
from moviepy.video.fx.all import loop
import moviepy.video.tools.drawing as mvpt
import re
import random

def create_film(title, comments):
    comment = comments[0].body
    
    # init audio
    audioclip = AudioFileClip("audio/" + re.sub(r'[^\w]', ' ', title) + ".mp3")
    video_audio = CompositeAudioClip([audioclip])

    # setup background
    ## make background videos random
    background = 0
    background = random.randrange(0,9)
    if background == 0:
        bg = VideoFileClip('bg_vids/Bike - 72566.mp4').loop(n=2)
    elif background == 1:
        bg = VideoFileClip('bg_vids/Ink - 67358.mp4').loop(n=2)
    elif background == 2:
        bg = VideoFileClip('bg_vids/Lemon - 82602.mp4').loop(n=2)
    elif background == 3:
        bg = VideoFileClip('bg_vids/Road - 84970.mp4').loop(n=2)
    elif background == 4:
        bg = VideoFileClip('bg_vids/Waterfall - 69786.mp4').loop(n=2)
    elif background == 5:
        bg = VideoFileClip('bg_vids/Nebula Blue - 49252.mp4').loop(n=2)
    elif background == 6:
        bg = VideoFileClip('bg_vids/Autumn Road - 91854.mp4')
    elif background == 7:
        bg = VideoFileClip('bg_vids/Candle - 93480.mp4')
    elif background == 8:
        bg = VideoFileClip('bg_vids/Grid - 82515.mp4').loop(n=6)
    elif background == 9:
        bg = VideoFileClip('bg_vids/Ocean - 83261.mp4').loop(n=2)
    elif background == 10:
        bg = VideoFileClip('bg_vids/River - 85373.mp4').loop(n=2)
    elif background == 11:
        bg = VideoFileClip('bg_vids/Skyscrapers - 80724.mp4').loop(n=2)
    elif background == 12:
        bg = VideoFileClip('bg_vids/Waves = 70796.mp4').loop(n=2)


    # add text to the background
    ## break text up into list based on periods

    ## place on screen
    screensize = (640,-1)
    text_collection = []
    starttime = 0.2

    text_clips=[]
    txt = TextClip(title, font='Courier',
                        fontsize=32, color="white", 
                        bg_color='#1f2021', method='caption',
                        size = screensize, kerning=-2, 
                        interline=-1, align='west')
    txt = txt.on_color(col_opacity=.3)
    txt = txt.set_position((20,500))
    txt = txt.margin(20, color=(31, 32, 33), top=30)
    txt = txt.set_start(starttime)
    txt = txt.set_duration(len(title)/20+(0.3 * (title.count("?") + 1)))
    starttime += len(title)/20+(0.3 * (title.count("?") + 1))
    text_clips.append(txt)
            
        
    textclip = CompositeVideoClip(text_clips)
    text_collection.append(textclip)

    
    sentences = []
    sentences.append("reddit asks")
    sentences.append(title)
    last = 0

    comment = comment.replace("\\n", "")
    
    for i in range(len(comment)):
        if i < (len(comment) - 1):
            if comment[i] == "." and comment[i+1] == " ":
                sentences.append(comment[last:i+1])
                last = i+1
            else:
                sentences.append(comment[last:i])
    for i in range(len(sentences)):
        txt = TextClip(sentences[i], font='Courier', 
                        fontsize=32, color="white", 
                        bg_color='#1f2021', method='caption',
                        size = screensize, kerning=-2, 
                        interline=-1, align='west')
        txt = txt.on_color(col_opacity=.3)
        txt = txt.set_position((20,500))
        txt = txt.margin(20, color=(31, 32, 33))
        txt = txt.set_start(starttime)
        txt = txt.set_duration(len(sentences[i])/20+(0.3 * (sentences[i].count("?") + 1)))
        starttime += len(sentences[i])/20+(0.3 * (sentences[i].count("?") + 1))
        text_clips.append(txt)
        

    # put it all together
    (w, h) = bg.size
    videoclip = bg.volumex(0)
    videoclip = crop(videoclip, width=720, height=1280, x_center=w/2, y_center=h/2)
    videoclip.audio = video_audio
    videoclip = videoclip.subclip(0, starttime)
    print(comment)
    videoclip = CompositeVideoClip([videoclip] + text_clips)

    videoclip.write_videofile(("exports/"+re.sub(r'[^\w]', ' ', title)).replace(" ","") + ".mp4")

#create_film("audio/What is the dumbest thing that people spend absurd amounts of money on .mp3")