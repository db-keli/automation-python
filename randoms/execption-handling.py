#!/usr/bin/python3

def spam(divideby):
	return 42 / divideby


print(spam(2))
# print(spam(0))....This line is a ZeroDivisionError


# Create an error exception for this

def e_spam(divideby):
	try:
		return 42 / divideby
	except ZeroDivisionError:
		print("Cannot divide an integer with 0")


e_spam(0)

