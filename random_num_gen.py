"""random number guessing game"""
__author__ = "Andrea Flack"

from random import randint
 	
def evaluation_of_guess():

	number_of_guesses = 0


	secret_numb = randint (1, 100)
	print(secret_numb)
	
	keep_looping = True 
	while keep_looping:	
		ask = input("I am thinking of a number between 1 and 100 what is it?  " )
		ask = int(ask)		
		number_of_guesses += 1

		if ask == secret_numb:
			print ("Good job!")
			keep_looping = False
			  
		elif number_of_guesses < 4:
			print ("Nope Dummy! Try again.")
		
		else:
			print("Bye Felisha")
			keep_looping = False
			
		
		  



evaluation_of_guess()


