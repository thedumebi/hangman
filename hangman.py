import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly choose a word from the list
    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user guessed.

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #tell the user the letters already used
        print(f"You have {lives} lives left and you have used these letters: ", " ".join(used_letters))

        #tell the user what the word is but with dashes where they haven't guessed eg W O _ D
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters: #alphabet - used_letters would give you a set of the letters in the alphabet not yet used.
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 #takes away a life if wrong
                print(f"Your letter {user_letter} is not in the word.")
        
        elif user_letter in used_letters:
            print("You have already used this letter before. Please try again.")

        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print(f"Sorry, you died. The word was {word}")
    else:
        print(f"You guessed the word {word} !!!")



hangman()