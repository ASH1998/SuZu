import sys, os.path

'''from https://stackoverflow.com/a/10038074/7454706'''

def all_from(folder='', abspath=None):
	"""add all dirs under `folder` to sys.path if any .py files are found.
	Use an abspath if you'd rather do it that way.

	Uses the current working directory as the location of using.py.
	Keep in mind that os.walk goes *all the way* down the directory tree.
	With that, try not to use this on something too close to '/'

	"""
	add = [] #set(sys.path) []
	if abspath is None:
		cwd = os.path.abspath(os.path.curdir)
		abspath = os.path.join(cwd, folder)
	for root, dirs, files in os.walk(abspath):
		for f in files:
			if f[-3:] in '.py':
				add.append(root)
				break
	for i in add:
		if "site-package" in i:
			continue
		# print(i)
		sys.path.append(i)