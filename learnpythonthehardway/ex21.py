#!/usr/bin/env python

def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a+b

def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a - b
def multiply(a,b):
	print "MULTIPLYING %d * %d" % (a,b)
	return a * b
def divide(a,b):
	print "DIVIDING %d / %d" % (a,b)
	return a / b

print "Let's do some math with just functions"
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(200, 1.5)
print "Age:%d,Height:%d,Weight:%d,IQ:%d" % (age,height,weight,iq)

what = add(age,subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes:",what,"Can you see"


'''
my function

'''
def domath(a,b,avg):
	print "NOW DO %d %r %d" % (a,avg,b)
	count = '%d%s%d' %(a,avg,b) 
	return eval(count)

abc = domath(20,10,'*')
print abc