#!/usr/bin/env python

import time, random

t = '2014-08-27 16:00:00'

def caipiao():
	timeStamp = int(time.mktime(time.strptime(t, '%Y-%m-%d %H:%M:%S')))
	print timeStamp
	random.seed(timeStamp)
	random_array = []
	for x in xrange(0,10):
		random_array.append(random.randint(0,9))

	print random_array
	print sorted(random_array) 
	total = 0
	for x in random_array:
		total += x
	print total

if __name__ == '__main__':
	caipiao()

