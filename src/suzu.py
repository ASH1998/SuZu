import os
import sys
import pandas as pd

from CustomExceptions import NotCompatibleException

class SuZu:
	def __init__(self, version):
		if version==2:
			raise NotCompatibleException
		else:
			print("version = ", version)

