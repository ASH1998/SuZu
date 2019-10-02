import sqlite3
from sqlite3 import Error
from ..logthings import get_module_logger
import traceback

log_app = get_module_logger("__DB__")

def create_connection(db_file):
	""" create a database connection to a SQLite database """
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		print(sqlite3.version)
	except Exception as e:
		log_app.info(str(e) + "  -  ", str(traceback.format_exc()))
	finally:
		if conn:
			conn.close()


if __name__ == '__main__':
	create_connection(r"pythonsqlite.db")