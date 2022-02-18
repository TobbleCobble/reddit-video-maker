from utils.redditScrape import scrapeComments
from utils.audioGenerator import soundify
from utils.captionCreate import commentImage, titleImage
from utils.videoCreate import createVideo

# Gets posts and top 5 comments from selected subreddit
### subreddit, number of posts, timeframe
subreddit= "askreddit"

post = scrapeComments(subreddit, 1, "day")

for i in range(len(post)):
    if i == 0:
        print(post[i].title)
        titleImage(post[i].title, "u/"+post[i].author.name, "r/"+subreddit)
    else:
        commentImage(post[i].author.name, post[i].body, i)

soundify(post)
createVideo(post[0].author.name)