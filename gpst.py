#!/usr/bin/python

import threading, time, urllib
from gps import *
import settings

# Based on example from Stack Overflow answer: <http://stackoverflow.com/questions/6146131/python-gps-module-reading-latest-gps-data>

class GpsPoller(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.session = gps(mode=WATCH_ENABLE)
		self.current_value = None

	def get_current_value(self):
		return self.current_value

	def run(self):
		try:
			while True:
				data = self.session.next()
				if data['class'] == u'TPV' and 'lat' in data.keys():
					self.current_value = data
		except StopIteration:
			pass

if __name__ == '__main__':
	gpsp = GpsPoller()
	gpsp.daemon = True # <http://stackoverflow.com/questions/1635080/terminate-a-multi-thread-python-program>
	gpsp.start()
	no_data = 0
	while 1:
		data = gpsp.get_current_value()
		if data:
			print(data.lat, data.lon)
			urllib.urlopen(settings.url, 'lat=%s&lon=%s' % (data.lat, data.lon))
		else:
			if no_data > 4:
				print('It seems like there will never be any data. Check that all hardware works as expected and/or try restarting the script.')
				break
			no_data += 1
			print('No data yet')	
		time.sleep(settings.interval)
