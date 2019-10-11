import praw

reddit = praw.Reddit('suzu', user_agent='suzu')



subreddit = reddit.subreddit('Naruto')

print(subreddit.display_name)  # Output: redditdev
print(subreddit.id)         # Output: reddit Development
# print(subreddit.description)
id = subreddit.id
submission = reddit.submission(id)
hot_python = subreddit.hot(limit=30)
for submission in hot_python:
	for top_level_comment in submission.comments:
		print(top_level_comment.body)