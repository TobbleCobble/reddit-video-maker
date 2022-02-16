from utils.redditScrape import scrapeComments
from utils.audioGenerator import soundify

# Gets posts and top 5 comments from selected subreddit
### subreddit, number of posts, timeframe
post = scrapeComments("askreddit", 1, "day")

soundify(post)

for i in range(len(post)):
    if i == 0:
        print(post[i].title)
    else:
        print(post[i].body)