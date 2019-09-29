import os
import sys

sys.path.append('SuzuException/')
from CustomExceptions import NotCompatibleException
from suzu import SuZu

global good_to_go

if sys.version[0]=='3' or sys.version[0]=='4':
	good_to_go=1
else:
	good_to_go=0

if good_to_go==0:
	try:
		version = sys.version[0]
		message = "You are using Python version " + str(version) + '.x, Use Python Version 3.x or 4.x'
		raise NotCompatibleException(message)
	except NotCompatibleException as e:
		print(e.reason())

if good_to_go==1:
	version = sys.version[0]
	SuZu(version)