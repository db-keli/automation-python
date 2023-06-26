#!/usr/bin/python3

def spam(divideBy):
	return 42 / divideBy

print(spam(2))
# print(spam(0))....This line is a ZeroDivisionError

#Create an error exception for this

def e_spam(divideBy):
	try:
		return 42/ divideBy
	except ZeroDivisionError:
		print("Cannot divide an integer with 0")

e_spam(0)
