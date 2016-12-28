#!/usr/bin/python

def division():
	print "Starting Math Problem"
	num1 = raw_input("What is the first number?")
	num2 = raw_input("What is the second number?")
	print "The Question is: %s / %s" % (num1, num2)
	test1 = int(num1)
	test2 = int(num2)
	div = test1 / test2
	print "The Answer is:"
	print div
division()

