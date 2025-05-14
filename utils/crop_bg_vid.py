import moviepy
import moviepy.editor 
import moviepy.video
import moviepy.video.fx
from moviepy.video.fx.all import crop
import moviepy.video.fx.resize

video_path = input("enter video path: ")
video = moviepy.editor.VideoFileClip(video_path)
video_output = input("enter video output path: ")

w, h = video.size
new_width = int(h * (9/16))
new_height = h


video = crop(video, width=new_width, height=new_height, x_center=w/2, y_center=h/2)
final_video = video.resize(width=720, height=1280)

final_video.write_videofile(video_output)