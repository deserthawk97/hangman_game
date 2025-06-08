import random
from  hangman_words import word_list
import hangman_art

print(hangman_art.logo)
print("\n")

# Below line choose a random word from the list.
chosen_word = random.choice(word_list)

#Variables
word_length = len(chosen_word)
guess = ""
result = ""
lives = 6
placeholder = ""
game_over = False

#create a list of letters for looping
guess_list = []
for i in chosen_word:
	guess_list.append(i)


#creates a placeholder like ------ with the length of guessed word
for i in range (word_length):
	placeholder += "_"
print(f"The pokemon to guess have {word_length} letters : {placeholder}")


display = list(placeholder)

#loops until the placeholder is not completed or the game is not over
while not game_over:
	print(f"\n\n*************You have {lives} lives left******************")
	print("Who's That Pokémon?")
	guess = input("Guess a letter: ")            					#Get input
	guess = guess.lower()
	if guess in display:
		print(f"You have already entered the letter '{guess}'..!! Please enter a different letter \n")
	for i in range(word_length):
		if guess == chosen_word[i]:                    				#Check for the match
			display[i] = guess						    			#append the guess word to list if it is  a match


	for i in range(word_length) :                      				#Convert list to string
		result=''.join(display)
	print("======================")
	print(f"Pokemon : {result}")
	print("======================")


	if guess not in chosen_word:                                    #Reduce the life for wrong guess
		lives = lives - 1
		print(f"You have guessed a wrong letter {guess} \n")
		print("The guy below will be hanged for wrong guess.")
		if lives == 0:
			game_over = True
			print("****************************************************************")
			print(f"\n\nGame over..!!!! \nThe chosen word is {chosen_word} \nYou Loose..!!!! Better luck next time")
			print("****************************************************************")

	print(hangman_art.stages[lives])  								#Print stage of life

	if "_" not in result:			 								#Check for a win
		game_over = True
		print("****************************************************************")
		print(f"The pokemon is {chosen_word} \nYou win..!!!! Congratulation.....!!!!")
		print(hangman_art.win)
		print("****************************************************************")












