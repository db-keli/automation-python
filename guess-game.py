#!/usr/bin/python3

import random

number = random.randint(1,3)
print("I am thinking of a number between 1 and 20.")
def guess():
	global guessv
	try:
			guessv = int(input("Take a guess: \n"))
			return guessv
	except ValueError:
		print("Invalid Input")
guess()
for i in range(1,7):
	if guessv < number:
		print("Your guess is too low.\n")
		guess()
	elif guessv > number:
		print("Your guess is too high.\n")
		guess()
	elif guessv == number:
		print("Good Job! You guessed my number right after %s guesse(s)!"% (str(i)))
		break
	else:
		break
print("The Number I was thinking of was %s" % (str(guessv)))

