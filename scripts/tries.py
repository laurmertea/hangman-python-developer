# Description
# Let's make the game iterative. 
# Now it's time to make the game resemble the classic version of Hangman a bit more. 
# The player should now guess letters in the word instead of typing the entire word all at once. 
# If the player guesses a letter, it should be uncovered in the word. 
# For now, start by building the defeat condition and add 8 tries to guess a letter that appears in the word. 
# When the player runs out of attempts, the game ends.
# Later we will determine the winning conditions, but in this stage, 
# let's just see how well our player guesses the word on each attempt.
#
# Objectives
# Now your game should work as follows:
# A player has exactly 8 tries and enters letters. 
# Nothing changes if a player has more tries left but they have already guessed the word.
# If the letter doesn't appear in the word, 
# the computer takes one try away – even if the user has already guessed this letter.
# If the player doesn't have any more attempts, the game should end and the program should show a losing message. 
# Otherwise, the player can continue to input letters.
# Also, the word should be selected from our list: 
# 'python', 'java', 'kotlin', 'javascript', 
# so that your program can be tested more reliably.
# Please, make sure that your program's output formatting precisely follows the example. 
# Pay attention to the empty lines between tries and at the end.
#
# Examples
# The greater-than symbol followed by space (> ) represents the user input. 
# Note that it's not part of the output.
# Example 1
# H A N G M A N
# ----------
# Input a letter: > a
# -a-a------
# Input a letter: > i
# -a-a---i--
# Input a letter: > o
# That letter doesn't appear in the word
# -a-a---i--
# Input a letter: > z
# That letter doesn't appear in the word
# -a-a---i--
# Input a letter: > l
# That letter doesn't appear in the word
# -a-a---ip-
# Input a letter: > p
# -a-a---ip-
# Input a letter: > h
# That letter doesn't appear in the word
# -a-a---ip-
# Input a letter: > k
# That letter doesn't appear in the word
# Thanks for playing!
# We'll see how well you did in the next stage
#
# Example 2
# H A N G M A N
# ----
# Input a letter: > j
# j---
# Input a letter: > i
# That letter doesn't appear in the word
# j---
# Input a letter: > g
# That letter doesn't appear in the word
# j---
# Input a letter: > o
# That letter doesn't appear in the word
# j---
# Input a letter: > a
# ja-a
# Input a letter: > v
# java
# Input a letter: > a
# java
# Input a letter: > j
# Thanks for playing!
# We'll see how well you did in the next stage

import random

GAME_TITLE = 'H A N G M A N'
GAME_SEP_LINE = '\n'
GAME_INPUT_MESSAGE = 'Guess the word '
GAME_INPUT_LETTER_MESSAGE = 'Input a letter: '
GAME_LETTER_NOT_FOUND_MESSAGE = 'That letter doesn\'t appear in the word'
GAME_SUCCESS_MESSAGE = 'You survived!'
GAME_FAIL_MESSAGE = 'You lost!'
GAME_END_MESSAGE = 'Thanks for playing!\nWe\'ll see how well you did in the next stage'
DEFAULT_TRIES = 8

words = ['python', 'java', 'kotlin', 'javascript']
computer_choice = random.choice(words)
hint = computer_choice[0:3:1] + "-" * (len(computer_choice) - 3)
tries = 0
found_letters = set()
mystery_word = "-" * len(computer_choice)

def search_letter(letter):
    global computer_choice
    global found_letters

    if letter in set(computer_choice):
        found_letters.add(letter)
    else:
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

while tries < DEFAULT_TRIES:
    tries += 1
    unmask()
    user_input = str(input(GAME_INPUT_LETTER_MESSAGE))
    search_letter(user_input)
    print(GAME_SEP_LINE)

print(GAME_END_MESSAGE)
