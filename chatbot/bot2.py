import praw
import time
import sqlite3
import os
from tqdm import tqdm



def writeintofile(filename, title):
	filename = filename+'.txt'

	if os.path.exists(filename):
		append_write = 'a' # append if already exists
	else:
		append_write = 'w' # make a new file if not

	with open(filename, append_write, encoding='utf-8') as fopen:
		for i in title:
			try:
				fopen.writelines(str(i) + '\n')
			except:
				continue


# reddit = praw.Reddit(client_id='zpyYkZKltt26Jg',
#                      client_secret='bdFmQeo_5gYb1be-dHytA0ON0So',
#                      user_agent='suzu')



def get_reddit(subredditname, limitno=1000, sleeptime=0.5, hottop='hot'):
	reddit = praw.Reddit('suzu', user_agent='suzu')

	# for submission in reddit.subreddit('learnpython').hot(limit=10):
	#     print(submission.title)

	subreddit = reddit.subreddit(subredditname)

	# print(subreddit.display_name)  # Output: redditdev
	# print(subreddit.id)         # Output: reddit Development
	# print(subreddit.description)
	id = subreddit.id
	submission = reddit.submission(id)
	if hottop=='hot':
		if limitno==-1:
			hot_python = subreddit.hot(limit=None)
		else:
			hot_python = subreddit.hot(limit=limitno)
	elif hottop=='top':
		if limitno==-1:
			hot_python = subreddit.top(limit=None)
		else:
			hot_python = subreddit.top(limit=limitno)
	else:
		hot_python = subreddit.hot(limit=limitno)

	titleslist = []
	commentslist = []
	replieslist = []
	titleno = 0

	subtitlelist = []
	subcommentlist = []
	subreplylist = []

	for submission in tqdm(hot_python):
		if titleno%20==0:
			writeintofile(hottop+'titles', subtitlelist)
			writeintofile(hottop+'replies', subreplylist)
			writeintofile(hottop+'comments', subcommentlist)
			subtitlelist = []
			subcommentlist = []
			subreplylist = []
		if titleno%50==0:
			time.sleep(sleeptime)
		try:
			if not submission.stickied:
				# print('Title: {}, ups: {}, downs: {}, Have we visited?: {}'.format(submission.title,
				# 																   submission.ups,
				# 																   submission.downs,
				# 																   submission.visited))

				titleno += 1
				titleslist.append([titleno, submission.title])
				subtitlelist.append([titleno, submission.title])
				comments = submission.comments
				commentno = 0
				for comment in comments:
					try:
						commentno += 1
						# print(20*'-')
						# print(comment.body)
						commentslist.append([titleno, commentno, comment.body])
						subcommentlist.append([titleno, commentno, comment.body])
						replyno = 0
						if len(comment.replies) > 0:
							for reply in comment.replies:
								try:
									replyno += 1
									# print('REPLY:')
									# print("\t"+reply.body)
									replieslist.append([titleno, commentno, replyno, reply.body])
									subreplylist.append([titleno, commentno, replyno, reply.body])
								except Exception as ee:
									# print(ee)
									continue
					except Exception as we:
						# print(we)
						pass

		except:
			continue

	return titleslist,  commentslist, replieslist

def createDB(db_file):
	""" create a database connection to a SQLite database """
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		# print(sqlite3.version)
	except Exception as e:
		#log_app.info(str(e) + "  -  ", str(traceback.format_exc()))
		pass
	finally:
		if conn:
			conn.close()


if __name__ == '__main__':
	title, comm, rep = get_reddit('manga', limitno=-1, sleeptime=5, hottop='top')
	# get_reddit('NN')
	# writeintofile('fullhottitle', title)
	# writeintofile('fullhotcomment', comm)
	# writeintofile('fullhotreply', rep)