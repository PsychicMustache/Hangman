# Cody Duran
# 2021/09/30

# importing necessary modules
import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)  # grabbing random word from list

# initializing variables
lives = 6
display = []  # this is used for the hidden word
users_guessed_letters = []  # this is used to hold the all the letters that have been guessed
end_of_game = False  # flag for main game loop
letter_added = False  # a flag to run statements necessary for taking away lives

print(hangman_art.logo + "\n")  # printing logo

for letter in chosen_word:
    display.append("_")  # adding "_" for each letter in chose_word

print(*display)  # display to the user the number of letters

# main game loop
while not end_of_game:
    guess = input("Please enter a letter: ").lower()  # ask user for letter

    # if user has already guessed inputted letter - let them know and go back to beginning of loop
    if guess in users_guessed_letters:
        print(f"\nYou have already guessed {guess}. Pick a different letter.")

    elif guess == "":
        print("You did not enter a letter . . . please enter a letter.\n")

    else:
        users_guessed_letters.append(guess)  # add letter to guessed letters
        for letterPosition in range(0,len(chosen_word)):  # running a loop to check if guess matches letter
            if guess == chosen_word[letterPosition]:
                display[letterPosition] = guess  # if so, replace "_" with letter
                letter_added = True  # setting flag to true so a life is not taken

        if letter_added == False:  # if a correct letter was not guessed, inform user and remove a life
            print(f"\nOh man . . . {guess} is NOT in the word.")
            lives -= 1

        print(hangman_art.stages[lives])  # show the gallow and hanged man (if applicable)
        print(*display)  # display remaining letters

        letter_added = False  # reset letter_added flag back to false

        # checking for end game situations
        if lives == 0:
            end_of_game = True
            print("\nYou LOSE!!!")
            print("The word was " + "'" + chosen_word + "'")
        elif "_" not in display:
            end_of_game = True
            print("\nYou WIN!!!")

