from types import NoneType
from utils.redditScrape import scrapeComments
from utils.audioGenerator import soundifyAuthor, soundifyComment
from utils.captionCreate import commentImage, titleImage
from utils.videoCreate import createVideo

import os
import time

# Gets posts and top 5 comments from selected subreddit
### subreddit, number of posts, timeframe
subreddit = "askreddit"


for i in range(10):
    #for file in os.listdir("temp"):
    #    os.remove("temp/"+file)
    
    postnum = i + 1
    post = scrapeComments(subreddit, postnum, "week")
    print(post[0].author)
    asker = str(post[0].author)
    os.makedirs(asker)
    for j in range(len(post)):
        
        if post[j].author is None:
            author = "[deleted]"
        else:
            try:
                author = post[j].author.name
            except:
                author = "[deleted]"
        
        if j == 0:
            print(post[j].title)
            titleImage(post[j].title, author, "r/"+subreddit)
        else:
            text = post[j].body
            print(text)
            sections = []
            if len(text) > 500:
                length = 0
                nextSpace = 0
                for k in range(len(text)):
                    if k % 300 == 0:
                        if text[k] == ".":
                            nextSpace = k + 2
                            sections.append(text[length:nextSpace])
                            length = nextSpace
                        else:
                            for l in range(len(text[:k])):
                                if text[l] == ".":
                                    nextSpace = l + 2
                                    
                            sections.append(text[length:nextSpace])
                            length = nextSpace

                sections.append(text[length:len(text)])
                sections = sections[1:]
            else:
                sections.append(text)
            
            for section in range(len(sections)):
                commentImage(author, sections[section], j, section, asker)
                soundifyComment(sections[section], j, section, asker)

    soundifyAuthor(post[0].title, asker)

    if post[0].author is None:
        author = "[deleted]"
    else:
        author = post[0].author.name
    createVideo(author)
    