import speech_recognition as sr
from voicetype_1 import voices
# create a speech recognition object
r = sr.Recognizer()
voice = voices()

# from pynput import keyboard

# def on_press(key):
# 	try:
# 		print('alphanumeric key {0} pressed'.format(
# 			key.char))
# 	except AttributeError:
# 		print('special key {0} pressed'.format(
# 			key))

# def on_release(key):
# 	print('{0} released'.format(
# 		key))
# 	if key:
# 		# Stop listener
# 		return False


# with keyboard.Listener(
# 		on_press=on_press,
# 		on_release=on_release) as listener:

with sr.Microphone() as source:
	# listen
	audio_data = r.record(source, duration=10)
	print('Recognizing...')
	# if 'stop' in str(listener):
    # 		text = r.recognize_google(audio_data)
	# 	voice.saypytt(text, volumerate=2.0, voicerate=200)
	# # convert to text

	# # Collect events until released
	# else:
	text = r.recognize_google(audio_data)
	voice.saypytt(text, volumerate=2.0, voicerate=200)

	# listener.join()
