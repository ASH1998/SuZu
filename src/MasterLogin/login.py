import sqlite3
from sqlite3 import Error
import pandas as pd
import traceback
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
# sys.path.append("..")
from src.logthings import get_module_logger
log_app = get_module_logger("__DB__")


def get_connection(db_file):
	""" create a database connection to a SQLite database """
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		# print(sqlite3.version)
		cur = conn.cursor()
		cur.execute("select id, name, password from userlogs")
		r = cur.fetchall()
		df = pd.DataFrame.from_records(r,columns=['id', 'user', 'pass'])
		#print(df)
		cur.close()
		conn.close()
		return df
	except Exception as e:
		log_app.info(str(e) + "  -  ", str(traceback.format_exc()))
		return 1


def addData(db_file):
	conn = sqlite3.connect(db_file)

