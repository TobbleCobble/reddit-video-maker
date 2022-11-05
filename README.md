# reddit-video-maker
makes TikTok style videos based on reddit posts and comments automatically 

## Setup:

Download all files

create files `bg_vids` and `exports` in main directory

add background videos in mov format to bg_vids, make sure they're inv `1080 x 1920` aspect ratio

Open main directory

 - `cd reddit-video-maker`

Install dependencies

 - `pip3 install moviepy praw PIL pyttsx3`

Change PRAW token information in redditScrape.py 

 - get all the stuff you need https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps
 - `reddit = praw.Reddit(
    client_id="yourClientID",
    client_secret="yourClientSecret",
    user_agent="<yourUserAgent>"
)`


run main.py from either longform or askreddit while still in main directory

 - `python3 longForm/main.py` or `python3 askreddit/main.py`
