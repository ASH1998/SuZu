import praw
import time
import sqlite3

reddit = praw.Reddit('suzu', user_agent='suzu')

# for submission in reddit.subreddit('learnpython').hot(limit=10):
#     print(submission.title)

subreddit = reddit.subreddit('Naruto')

# print(subreddit.display_name)  # Output: redditdev
# print(subreddit.id)         # Output: reddit Development
# print(subreddit.description)
id = subreddit.id
submission = reddit.submission(id)
hot_python = subreddit.hot(limit=10)

titleslist = []
commentslist = []
replieslist = []
titleno = 0

for submission in hot_python:
	try:
		if not submission.stickied:
			# print('Title: {}, ups: {}, downs: {}, Have we visited?: {}'.format(submission.title,
			# 																   submission.ups,
			# 																   submission.downs,
			# 																   submission.visited))

			titleno += 1
			titleslist.append([titleno, submission.title])
			comments = submission.comments
			commentno = 0
			for comment in comments:
				try:
					commentno += 1
					# print(20*'-')
					# print(comment.body)
					commentslist.append([titleno, commentno, comment.body])
					replyno = 0
					if len(comment.replies) > 0:
						for reply in comment.replies:
							try:
								replyno += 1
								# print('REPLY:')
								# print("\t"+reply.body)
								replieslist.append([titleno, commentno, replyno, reply.body])
							except Exception as ee:
								print(ee)
								continue
				except Exception as we:
					print(we)
					pass

	except:
		continue

print(replieslist)
print(len(commentslist))
print(len(replieslist))