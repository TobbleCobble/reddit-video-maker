import praw

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent=""
)

def get_posts(sub, count, span):
    subreddit = reddit.subreddit(sub)
    posts = []
    for submission in subreddit.top(span, limit=count):
        if "r/" not in submission.title and "reddit" not in submission.title:
            posts.append(submission)

    return posts


def scrapeComments(subreddit, count, span):
    posts = get_posts(subreddit, count, span)
    postText = []
    #postText = [posts[0],posts[0].selftext]
    for i in range(count):
        postText.append([posts[i],posts[i].selftext])

    return postText

if __name__ == "__main__":
    post = scrapeComments("nosleep", 1, "day")
    print(post)
    print(post[0].author)
