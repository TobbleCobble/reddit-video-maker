# reddit-video-maker
makes TikTok style videos based on reddit posts and comments automatically 

## Setup:

Download all files

add background videos in mp4 or mov format to bg_vids
resize these videos using `python3 crop_bg_vid.py` if they aren't already `720 x 1280`

add any background music in wav or mp3 format to the `music` folder

Open main directory

 - `cd reddit-video-maker`

Install dependencies

 - `pip3 install moviepy praw pillow pyttsx3`


Create a new reddit application
- https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps

create `client_details.json` with the following details from your reddit app:
``` 
reddit = praw.Reddit (
    client_id="yourClientID",
    client_secret="yourClientSecret",
    user_agent="yourUserAgent"
) 
```

run main.py

 - `python3 main.py`
