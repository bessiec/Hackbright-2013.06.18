import random

def guess_my_number():
	print "What is your name?"
	name = raw_input()

	print "Hi %s, I am thinking of a number between 1 and 100.  Try to guess my number." %name

	number = random.randint(1,100)
	# print "%r" %number

	guess = 0
	number_tries = 0
	

	while guess != number: 
		guess = int(raw_input())  

		number_tries += 1

		if guess > number: 
			print "Your guess is too high"
			print "Your guess:", guess
		elif guess < number:
			print "Your guess is too low"
			print "Your guess:", guess
		else: 
			print "Congratualations!  You guessed my number!"
			print "Well done, %s! You found my number in %d tries." %(name,number_tries)
			
# To call function
#guess_my_number()


def guess_my_num():
	print "What is your name?"
	name = raw_input()

	print "Hi %s, I am thinking of a number between 1 and 100.  Try to guess my number." %name

	number = random.randint(1,100)
	print "%r" %number

	
	continue_game =True
	number_tries = 0

	while True: 
		guess = int(raw_input())  

		number_tries += 1

		if guess > number: 
			print "Your guess is too high"
			print "Your guess:", guess
		elif guess < number:
			print "Your guess is too low"
			print "Your guess:", guess
		else: 
			print "Congratualations!  You guessed my number!"
			print "Well done, %s! You found my number in %d tries." %(name,number_tries)
			continue_game= False

# To call function
#guess_my_num()
