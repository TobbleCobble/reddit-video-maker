from venv import create
import pyttsx3
import praw
import re
from utils.videoCreater import create_film


def synthesise(text, title):
    engine = pyttsx3.init()
    engine.save_to_file(text, "audio/"+title)
    engine.runAndWait()

reddit = praw.Reddit(
    client_id="cNd2mIIhZmzBcsAHeeHo9g",
    client_secret="p68JnkeUTu68IeGavpvzR3OYsQ2O8Q",
    user_agent="<AutoTubeBot-v0.1>"
)

def get_posts(sub):
    subreddit = reddit.subreddit(sub)
    posts = []
    for submission in subreddit.top("day", limit=5):
        if "r/" not in submission.title:
            posts.append(submission)

    return posts

def save_image(submission):
            #cv2.imwrite(f"{image_path}", image)
        submission.comment_sort = 'best'

        comments = []

            # Get best comment.
        best_comment = None
        best_comment_2 = None

        for top_level_comment in submission.comments:
                    # Here you can fetch data off the comment.
                    # For the sake of example, we're just printing the comment body.
            
            
            # get top comment
            if "http" not in top_level_comment.body:
                #if len(top_level_comment.body) > 140:
                #    best_comment = top_level_comment
                #    comments.append(best_comment)
                #    break
                if len(top_level_comment.body) <= 140:
                    if best_comment is None:
                        best_comment = top_level_comment
                        comments.append(best_comment)
                        break
                    else:
                        best_comment_2 = top_level_comment
                        comments.append(best_comment_2)
                        break

        best_comment.reply_sort = "top"
        best_comment.refresh()

        return comments


posts = get_posts("askreddit")
for post in posts:
    title = post.title
    comment = save_image(post)
    print(title)
    synthesise("reddit asks \n" + re.sub(r'[^\w]', ' ', post.title) + "\n \n" + comment[0].body, re.sub(r'[^\w]', ' ', post.title) + ".mp3")
    create_film(title, comment)

