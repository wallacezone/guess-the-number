# ------------------------------------------------------------------
#
# Guess The Number (v1.0)
#
# A simple game by Alessandro Barbieri
#
# Code available at: https://github.com/wallacezone/guess-the-number
#
# ------------------------------------------------------------------

import random, sys

# -------------------------- VARS & FUNCS --------------------------

# main game
def game():

	# ask for the number of digits
	print(' How many digits? (3-10)')
	print()
	while True:
		digits = input(' > ')
		print()
		
		# input must be a number between 3 and 10
		try:
			if int(digits) < 3 or int(digits) > 10:
				print(' Input a number between 3 and 10!')
				print()
				continue
			break
		except ValueError:
			print(' That is not a valid number!')
			print()
	print(' You have ' + str(int(digits)**2) + ' attempts to guess the number of ' + digits + ' digits!')
	print()

	# create random number
	number = ''
	for i in range(int(digits)):
		number += str(random.randint(0, 9))

	# cycle through attempts
	i = 0
	while True:

		# increment i
		i += 1

		# check whether max num of attempts reached
		if i == int(digits)**2:
			break

		# player guess
		print(' Try to guess! Attempt n. ' + str(i))
		print()
		while True:
			guess = input(' > ')
			print()

			# input must be a number and must have n digits
			try:
				int(guess)
				if len(guess) != int(digits):
					print(' You must input a number of ' + str(digits) + ' digits!')
					print()
					continue
				break
			except ValueError:
				print(' That is not a valid number!')
				print()

		# if the number is guessed return
		if int(guess) == int(number):
			print(' Congratulations! You have guessed the number in ' + str(i) + ' attempts!')
			print()
			return
				
		# else check every digit
		clue = ' > '
		for j in range(len(guess)):

			# check if digit is in the right place
			if guess[j] == number[j]:
				clue += 'O'

			# else check if the digit is in the wrong place
			elif guess[j] in number:
				clue += 'o'

			# else check if the digit is wrong
			else:
				clue += 'X'

		# print clue
		print(clue)
		print()

	# if num not guessed
	print(' You have not guessed the number in ' + str(int(digits)**2) + ' attempts!')
	print()

# print the title
def print_title():
	print()
	print(' ------------------------ Guess The Number ------------------------')
	print()
	print(' Code available at: https://github.com/wallacezone/guess-the-number')
	print()
	print(' You have to guess a number of n digits')
	print(' When you input a wrong digit, the program returns \'X\'')
	print(' When you input a digit in the wrong pisition, the program returns \'o\'')
	print(' When you input a digit in the correct position, the program returns \'O\'')
	print(' You have n^2 attempts to guess the right number')
	print()

# start the game
def start():

	while True:

		# loop the main game
		game()

		# ask if player wants to play again
		print(' Do you want to play again? (y/n)')
		print()
		choice = ''
		while choice != 'y' and choice != 'n':
			choice = input(' > ')
			print()
			if choice == 'n':
				exit(0)

# ------------------------------ MAIN ------------------------------

print_title()

start()