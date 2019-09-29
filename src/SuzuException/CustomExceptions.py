class NotCompatibleException(Exception):
	def __init__(self, payload=None, message='Incompatible'):
		self.message = message
		self.payload = payload

	def __str__(self):
		return str(self.message)  # __str__()
	def reason(self):
		return str("|" + self.message + " : " + self.payload + "|")
