from types import NoneType
from utils.redditScrape import scrapeComments
from utils.audioGenerator import soundifyAuthor, soundifyComment
from utils.captionCreate import commentImage, titleImage
from utils.videoCreate import createVideo

import os
import textwrap
import shutil

# Gets posts and top 5 comments from selected subreddit
### subreddit, number of posts, timeframe
subreddit = "tifu"
count = 5


post = scrapeComments(subreddit, count, "week")
for i in range(count):
    print(post[i][0].author)


    if post[i][0].author is None:
        author = "[deleted]"
    else:
        author = str(post[i][0].author)

    try:
        shutil.rmtree(author)
    except OSError:
        pass

    os.makedirs(author)

    print(post[i][0].title)
    titleImage(post[i][0].title, author, "r/"+subreddit)    


    text = post[i][1]

    sections = textwrap.wrap(text, width=250)

    for section in range(len(sections)):
        commentImage(author, sections[section], 1, section+1, author)
        soundifyComment(sections[section], 1, section, author)

    soundifyAuthor(post[i][0].title, author)


    createVideo(author)

    try:
        shutil.rmtree(author)
    except OSError:
        pass
    