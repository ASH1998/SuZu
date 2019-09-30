import pyttsx3
from win32com.client import Dispatch

class voices:
	def __init__(self, setvoice=1):
		self.setvoice = 1
		self.engine = pyttsx3.init()
	def saypytt(self, message='hello', voicegender=1, volumerate=0.9, voicerate=200):
		'''
		:param message: message you want to say, str
		:param voicegender: male or female voice, 0/1.
		:param volume: float(0-1)
		:param voicerate: int, 200 is a good rate
		:return:
		'''

		voices = self.engine.getProperty('voices')
		if voicegender==0:
			self.engine.setProperty('voice', voices[0].id)
		else:
			self.engine.setProperty('voice', voices[1].id)

		self.engine.setProperty('rate', voicerate)


		self.engine.setProperty('volume', volumerate)

		self.engine.say(str(message))
		self.engine.runAndWait()



v = voices()

v.saypytt("yo whatsup!! My name is Suzu. I am well. How are you ?", volumerate=2.0, voicerate=200)





