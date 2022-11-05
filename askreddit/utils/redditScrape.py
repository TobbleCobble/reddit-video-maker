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

def get_comments(submission):
    submission.comment_sort = 'best'

    comments = []

    for top_level_comment in submission.comments:
        
        # make sure it's not a link and get top 6 comments
        if "http" not in top_level_comment.body and len(comments) < 6:
            comments.append(top_level_comment)
        elif len(comments) >= 6:
            break

    return comments

def scrapeComments(subreddit, count, span):
    posts = get_posts(subreddit, count, span)
    

    for post in posts:
        got_comments = get_comments(post)

        for comment in got_comments:
            if len(comment.body) > 800:
                got_comments = [comment]
                break
        comments=[post]
        length = 0
        # return as many comments that are under 1000 characters (~200 words)
        for comment in range(len(got_comments)):
            length += len(got_comments[comment].body)
            if length > 1000 and comment > 0:
                break
            else:
                comments.append(got_comments[comment])

    return comments

if __name__ == "__main__":
    scrapeComments("askreddit", 1, "day")
