import logging
import os

def get_module_logger(mod_name='__mainlog__'):
	filename = 'Logs'
	if not os.path.exists(filename):
		os.makedirs(filename)
	logging.basicConfig(filename='Logs\\'+mod_name+'.log', level=logging.INFO)
	logger = logging.getLogger('Logs\\'+mod_name+'.log')
	handler = logging.StreamHandler()
	formatter = logging.Formatter(
		'%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	logger.setLevel(logging.INFO)
	return logger