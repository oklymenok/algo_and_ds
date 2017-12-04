#!/usr/bin/python
import os
import time

try:
	print "Parent process: %d" % os.getpid()
	print "Trying to fork"
	p = os.fork()
except Exception:
	print "Couldn't fork"
else:
	if p>0:
		print "This is parent process: %d" % os.getpid()
		print "Waiting for child to become a zombie"
		time.sleep(30)
		print "Reaping zombie process"
		pid,exit_code = os.wait()
		print "Child process %d finished with %d code" % (pid,exit_code)
	else:
		print "This is child process: %d" % os.getpid()
		print "Living a short process life"
		time.sleep(10)
		print "Now become a zombie"
