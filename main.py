import os
#import tkinter as tk
from utils.redditScrape import scrapeText, scrapeComments
from utils.audioGenerator import soundifyAuthor, soundifyPost, soundifyComment
from utils.captionCreate import titleImage, textImage, commentImage
from utils.videoCreate import createVideo

import os
import textwrap
import shutil

#root = tk.Tk()

subreddit = ""
count = 1
span = "week"

video_type = input("enter video type (lf/ar): ")
count = int(input("enter video count (1-10): "))
span = input("enter time range (day/week): ")


def long_form():
    posts = scrapeText(subreddit, count, "week")

    for post in posts:
        print("Author: ", post[0].author)

        if post[0].author is None:
            author = "[deleted]"
        else:
            author = str(post[0].author)

        try:
            shutil.rmtree("temp/"+author)
        except OSError:
            pass

        os.makedirs("temp/"+author)

        print(post[0].title)
        titleImage(post[0].title, author, "r/"+subreddit)    
        text = post[1]
        sections = textwrap.wrap(text, width=400)
        if len(text) > 5000:
            print("[INFO]: length of post is too long")
            continue
        for section in range(len(sections)):
            textImage(author, sections[section], 1, section+1)
            soundifyPost(sections[section], 1, section, author)

        soundifyAuthor(post[0].title, author)


        createVideo(author)

        try:
            shutil.rmtree(author)
        except OSError:
            pass

def askreddit():
    posts = scrapeComments("askreddit", count, span)
    
    for post in posts:
        if post == None:
            quit()

        print("Author: ", post[0].author)
        asker = str(post[0].author)
        
        if os.path.isdir("temp/"+asker):
            shutil.rmtree("temp/"+asker)
        
        subreddit = str(post[0].subreddit)
        
        os.makedirs("temp/"+asker)

        for j in range(len(post)):
            if post[j].author is None:
                author = "[deleted]"
            else:
                try:
                    author = post[j].author.name
                except:
                    author = "[deleted]"
            if j == 0:
                print("Title: ", post[j].title)
                titleImage(post[j].title, author, "r/"+subreddit)
            else:
                text = post[j].body
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

match video_type:
    case "lf":
        subreddit = input("what subreddit: ")
        long_form()
    case "ar":
        askreddit()