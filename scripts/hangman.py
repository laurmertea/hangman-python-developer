# Description
# We're almost done!
# Let's add a little more flavor to the game by adding a suggestion to replay the game after the current session ends.
#
# Objectives
# The game starts with a menu where a player can choose to either play or exit.
# Print Type "play" to play the game, "exit" to quit: and show this message again if the player inputs something else.
# If the user chooses to play, the game begins.
# Please, make sure that your program's output formatting precisely follows the output formatting in the example. 
# Pay attention to the empty lines between tries and in the end.
#
# Example
# The greater-than symbol followed by space (> ) represents the user input. Note that it's not part of the output.
#
# H A N G M A N
# Type "play" to play the game, "exit" to quit: > play
# 
# ----------
# Input a letter: > a
#
# -a-a------
# Input a letter: > i
#
# -a-a---i--
# Input a letter: > o
# That letter doesn't appear in the word
#
# -a-a---i--
# Input a letter: > o
# You've already guessed this letter
#
# -a-a---i--
# Input a letter: > p
# 
# -a-a---ip-
# Input a letter: > p
# You've already guessed this letter
# 
# -a-a---ip-
# Input a letter: > h
# That letter doesn't appear in the word
# 
# -a-a---ip-
# Input a letter: > k
# That letter doesn't appear in the word
#
# -a-a---ip-
# Input a letter: > a
# You've already guessed this letter
#
# -a-a---ip-
# Input a letter: > z
# That letter doesn't appear in the word
#
# -a-a---ipt
# Input a letter: > t
#
# -a-a---ipt
# Input a letter: > x
# That letter doesn't appear in the word
#
# -a-a---ipt
# Input a letter: > b
# That letter doesn't appear in the word
#
# -a-a---ipt
# Input a letter: > d
# That letter doesn't appear in the word
#
# -a-a---ipt
# Input a letter: > w
# That letter doesn't appear in the word
# You lost!
#
# Type "play" to play the game, "exit" to quit: > exit

import sys
import random
import string

GAME_TITLE = "H A N G M A N"
GAME_MENU = 'Type "play" to play the game, "exit" to quit: '

words = ['python', 'java', 'kotlin', 'javascript']
menu = ['play', 'exit']
selected_menu_option = None

class Hangman:
    INPUT_MESSAGE = "Guess the word "
    INPUT_LETTER_MESSAGE = "Input a letter: "
    LETTER_NOT_FOUND_MESSAGE = "That letter doesn't appear in the word"
    SUCCESS_MESSAGE = "You survived!"
    FAIL_MESSAGE = "You lost!"
    UNSUPPORTED_INPUT = "Please enter a lowercase English letter"
    INCORRECT_INPUT_LENGTH = "You should input a single letter"
    ALREADY_GUESSED = "You've already guessed this letter"
    END_MESSAGE = "Thanks for playing!\nWe'll see how well you did in the next stage"
    DEFAULT_NUMBER_OF_TRIES = 8

    def __init__(self, words=words):
        self.words = words
        self.tries = 0
        self.max_tries = self.DEFAULT_NUMBER_OF_TRIES
        self.computer_choice = random.choice(words)
        self.current_guessed = ''
        self.valid = False
        self.guessed = False
        self.found_letters = set()
        self.tried_letters = set()
        self.mystery_word = "-" * len(self.computer_choice)

    def search_letter(self, letter):
        if letter in self.tried_letters:
            print(self.ALREADY_GUESSED)
        else:
            if letter in set(self.computer_choice):
                if letter in self.found_letters:
                    print(self.ALREADY_GUESSED)            
                else:
                    self.found_letters.add(letter)
            else:
                self.tried_letters.add(letter)
                self.tries += 1
                print(self.LETTER_NOT_FOUND_MESSAGE)
    
    def unmask(self):
        masked = "-" * len(self.computer_choice)
        masked_list = [*masked]
        for letter in self.found_letters:
            for index, char in enumerate([*self.computer_choice]):
                if letter == char:
                    masked_list[index] = letter
        return ''.join(masked_list)

    def main(self):
        while self.tries < self.max_tries and self.guessed != True:
            if self.tries < self.max_tries:
                if self.guessed != True:
                    while self.valid == False:
                        self.current_guessed = self.unmask()
                        if self.current_guessed == self.computer_choice:
                            self.guessed = True
                            break
                        print("\n" + self.current_guessed)
                        user_input = str(input(self.INPUT_LETTER_MESSAGE))
                        if len(user_input) == 1 and all((True if char in string.ascii_lowercase else False for char in user_input)) == True:
                            self.valid = True
                        else:
                            if len(user_input) != 1:
                                print(self.INCORRECT_INPUT_LENGTH)
                            if all((True if char in string.ascii_lowercase else False for char in user_input)) == False:
                                print(self.UNSUPPORTED_INPUT)
                    if self.guessed != True:
                        self.search_letter(user_input)
                        self.valid = False
                    else:
                        print(self.SUCCESS_MESSAGE)
        if not self.guessed:
            print(self.FAIL_MESSAGE)
            
print(GAME_TITLE)
while selected_menu_option != "exit":
    while selected_menu_option not in menu:
        selected_menu_option = str(input(GAME_MENU))
    if selected_menu_option == "exit":
        sys.exit()
    game = Hangman(words)
    game.main()
    selected_menu_option = str(input(GAME_MENU))
