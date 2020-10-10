# Description
# The most recent version of the game is not so much fun, 
# since we still don’t have a way to handle the player's victory. 
# The player has 8 attempts to guess letters, 
# and the number of remaining attempts decreases after each try even if the player guesses correctly.
# In this next version, a player may get a lot of attempts 
# because they are limited only by the number of mistakes they make. 
# A player can be mistaken 8 times. 
# They win when they have guessed all the letters and still have at least one try. 
# If the player uses their last try and actually guesses the word, then they’ve won!
#
# Objectives
# The player starts the game with 8 "lives", which is to say, our player can input a wrong letter 8 times.
# Print That letter does not appear in the word and reduce the number of remaining attempts 
# if the word selected by the program doesn't contain this letter.
# Print No improvements and reduce the attempts count if the selected word contains this letter 
# but the user has already tried guessing it.
# The number of remaining attempts should be decreased only if there are no letters to uncover.
# Please, make sure that your program's output formatting precisely follows the output formatting in the example. 
# Pay attention to the empty lines between tries and at the end.
#
# Examples
# The greater-than symbol followed by space (> ) represents the user input. 
# Note that it's not part of the output.
# Example 1
# H A N G M A N
#
# ------
# Input a letter: > t
# 
# --t---
# Input a letter: > z
# That letter doesn't appear in the word
# 
# --t---
# Input a letter: > t
# No improvements
# 
# --t---
# Input a letter: > t
# No improvements
# 
# --t---
# Input a letter: > y
# 
# -yt---
# Input a letter: > x
# That letter doesn't appear in the word
# 
# -yt---
# Input a letter: > y
# No improvements
# 
# -yt---
# Input a letter: > p
# 
# pyt---
# Input a letter: > p
# No improvements
# 
# pyt---
# Input a letter: > q
# That letter doesn't appear in the word
# 
# pyt---
# Input a letter: > p
# No improvements
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
# Input a letter: > g
# That letter doesn't appear in the word
# 
# j---
# Input a letter: > g
# That letter doesn't appear in the word
# 
# j---
# Input a letter: > g
# That letter doesn't appear in the word
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
# 
# java
# You guessed the word!
# You survived!

import random

GAME_TITLE = 'H A N G M A N'
GAME_SEP_LINE = '\n'
GAME_INPUT_MESSAGE = 'Guess the word '
GAME_INPUT_LETTER_MESSAGE = 'Input a letter: '
GAME_LETTER_NOT_FOUND_MESSAGE = 'That letter doesn\'t appear in the word'
GAME_SUCCESS_MESSAGE = 'You survived!'
GAME_FAIL_MESSAGE = 'You lost!'
GAME_ALREADY_GUESSED = 'No improvements'
GAME_END_MESSAGE = 'Thanks for playing!\nWe\'ll see how well you did in the next stage'
DEFAULT_TRIES = 8

words = ['python', 'java', 'kotlin', 'javascript']
computer_choice = random.choice(words)
hint = computer_choice[0:3:1] + "-" * (len(computer_choice) - 3)
tries = 0
guessed = False
found_letters = set()
mystery_word = "-" * len(computer_choice)

def search_letter(letter):
    global computer_choice
    global found_letters
    global tries

    if letter in set(computer_choice):
        if letter in found_letters:
            tries += 1
            print(GAME_ALREADY_GUESSED)
        else:
            found_letters.add(letter)
    else:
        tries += 1
        print(GAME_LETTER_NOT_FOUND_MESSAGE)

print(GAME_TITLE)
print(GAME_SEP_LINE)

def unmask():
    global computer_choice
    global found_letters

    masked = "-" * len(computer_choice)
    masked_list = [*masked]

    for letter in found_letters:
        for index, char in enumerate([*computer_choice]):
            if letter == char:
                masked_list[index] = letter

    print(''.join(masked_list))
    return ''.join(masked_list)

while tries < DEFAULT_TRIES:
    current_guessed = unmask()
    if current_guessed != computer_choice:
        user_input = str(input(GAME_INPUT_LETTER_MESSAGE))
        search_letter(user_input)
        if tries < 8:
            print(GAME_SEP_LINE)
    else:
        print(GAME_SUCCESS_MESSAGE)
        guessed = True
        break        
if not guessed:
    print(GAME_FAIL_MESSAGE)
print(GAME_END_MESSAGE)
