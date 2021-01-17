import praw
import credentials

file = open("tickers.txt", "r")
words = file.read().splitlines()
file.close()

reddit = praw.Reddit(
    client_id = credentials.client_id,
    client_secret = credentials.client_secret,
    user_agent = credentials.user_agent
)

subreddit = reddit.subreddit("investing")

for submission in subreddit.hot(limit = 60):
    print(submission.title)