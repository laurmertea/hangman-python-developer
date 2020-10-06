# Description
# If there is a predefined word, the game isn't replayable. 
# You already know the word, so there’s no longer any challenge. 
# At this stage, let's make the game more challenging by choosing a word from a special list with a variety of options. 
# This way, our game will have more replay value.
#
# Objectives
# Create the following list of words: 'python', 'java', 'kotlin', 'javascript'.
# Program the game to choose a word from the list at random. You can enter more words, but let's stick to these four for now.
#
# Examples
# The greater-than symbol followed by space (> ) represents the user input. Note that it's not part of the output.
# Example 1, The computer randomly chose python from the list.
# H A N G M A N
# Guess the word: > python
# You survived!
#
# Example 2, the computer randomly chose something other than python from the list.
# H A N G M A N
# Guess the word: > python
# You lost!
#
# Example 3, the computer randomly chose something other than kotlin from the list.
# H A N G M A N
# Guess the word: > kotlin
# You lost!

import random

GAME_TITLE = 'H A N G M A N'
GAME_INPUT_MESSAGE = 'Guess the word: '
GAME_SUCCESS_MESSAGE = 'You survived!'
GAME_FAIL_MESSAGE = 'You lost!'

words = ['python', 'java', 'kotlin', 'javascript']

print(GAME_TITLE)
user_input = str(input(GAME_INPUT_MESSAGE))

if user_input == random.choice(words):
    print(GAME_SUCCESS_MESSAGE)
else:
    print(GAME_FAIL_MESSAGE)
