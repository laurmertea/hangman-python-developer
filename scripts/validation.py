# Description
# Now that we are done with the basics, let's work on perfecting some details.
# In the previous stage, if the user entered the same letter twice, 
# the program reduced the number of remaining attempts regardless of whether this was a correct letter or not. 
# This doesn’t seem fair to the player, does it? 
# They gain no additional information about the situation on the field yet the program still reduces their remaining attempts. 
# Let's fix it!
#
# Objectives
# If the user enters the same letter twice, then the program should output You've already guessed this letter.
# Also, you should check to make sure the player entered an English lowercase letter. 
# If not, the program should print Please enter a lowercase English letter.
# You should also check if the player entered exactly one letter. 
# If not, the program should print You should input a single letter. Remember that zero is also not one!
# Note that none of these three errors should reduce the number of remaining attempts!
# Please, make sure that your program's output formatting precisely follows the output formatting in the example. 
# Pay attention to the empty lines between tries and in the end.
#
# Examples
# The greater-than symbol followed by space (> ) represents the user input. Note that it's not part of the output.
# Example 1
# H A N G M A N
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
# Example 2
# H A N G M A N
# 
# ----
# Input a letter: > j
# 
# j---
# Input a letter: > i
# That letter doesn't appear in the word
# 
# j---
# Input a letter: > +
# Please enter a lowercase English letter
#
# j---
# Input a letter: > A
# Please enter a lowercase English letter
#
# j---
# Input a letter: > ii
# You should input a single letter
# 
# j---
# Input a letter: > ++
# You should input a single letter
# 
# j---
# Input a letter: >
# You should input a single letter
#
# j---
# Input a letter: > g
# That letter doesn't appear in the word
#
# j---
# Input a letter: > a
#
# ja-a
# Input a letter: > v
# You guessed the word java!
# You survived!

import random
import string

GAME_TITLE = "H A N G M A N"
GAME_INPUT_MESSAGE = "Guess the word "
GAME_INPUT_LETTER_MESSAGE = "Input a letter: "
GAME_LETTER_NOT_FOUND_MESSAGE = "That letter doesn't appear in the word"
GAME_SUCCESS_MESSAGE = "You survived!"
GAME_FAIL_MESSAGE = "You lost!"
GAME_UNSUPPORTED_INPUT = "Please enter a lowercase English letter"
GAME_INCORRECT_INPUT_LENGTH = "You should input a single letter"
GAME_ALREADY_GUESSED = "You've already guessed this letter"
GAME_END_MESSAGE = "Thanks for playing!\nWe'll see how well you did in the next stage"
DEFAULT_TRIES = 8

words = ['python', 'java', 'kotlin', 'javascript']
computer_choice = random.choice(words)
current_guessed = ''
tries = 0
valid = False
guessed = False
found_letters = set()
tried_letters = set()
mystery_word = "-" * len(computer_choice)

def search_letter(letter):
    global computer_choice
    global found_letters
    global tried_letters
    global tries

    if letter in tried_letters:
        print(GAME_ALREADY_GUESSED)
    else:
        if letter in set(computer_choice):
            if letter in found_letters:
                print(GAME_ALREADY_GUESSED)            
            else:
                found_letters.add(letter)
        else:
            tried_letters.add(letter)
            tries += 1
            print(GAME_LETTER_NOT_FOUND_MESSAGE)           

def unmask():
    global computer_choice
    global found_letters

    masked = "-" * len(computer_choice)
    masked_list = [*masked]

    for letter in found_letters:
        for index, char in enumerate([*computer_choice]):
            if letter == char:
                masked_list[index] = letter

    print("\n" + ''.join(masked_list))
    return ''.join(masked_list)

print(GAME_TITLE)

while tries < DEFAULT_TRIES:
    if current_guessed != computer_choice:
        while valid == False:
            current_guessed = unmask()
            user_input = str(input(GAME_INPUT_LETTER_MESSAGE))
            if len(user_input) == 1 and all((True if char in string.ascii_lowercase else False for char in user_input)) == True:
                valid = True
            else:
                if len(user_input) != 1:
                    print(GAME_INCORRECT_INPUT_LENGTH)
                if all((True if char in string.ascii_lowercase else False for char in user_input)) == False:
                    print(GAME_UNSUPPORTED_INPUT)
        search_letter(user_input)
        valid = False
    else:
        print(GAME_SUCCESS_MESSAGE)
        guessed = True
        break        
if not guessed:
    print(GAME_FAIL_MESSAGE)
