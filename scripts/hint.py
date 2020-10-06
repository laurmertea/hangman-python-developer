# Description
# Now our game has become quite hard, and your chances of guessing the word depend on the size of the list. 
# When the list has four words, you only have a 25% chance to guess correctly. 
# So let's show a little mercy to the player and add a hint for them.
#
# Objectives
# As in the previous stage, you should use the following word list: 'python', 'java', 'kotlin', 'javascript'
# Once the computer has chosen a word from the list, show its first 3 letters. Hidden letters should be replaced with hyphens ("-").
#
# Examples
# The greater-than symbol followed by space (> ) represents the user input. Note that it's not part of the output.
# Example 1
# H A N G M A N
# Guess the word jav-: > java
# You survived!
#
# Example 2
# H A N G M A N
# Guess the word pyt---: > pythia
# You lost!

import random

GAME_TITLE = 'H A N G M A N'
GAME_INPUT_MESSAGE = 'Guess the word '
GAME_SUCCESS_MESSAGE = 'You survived!'
GAME_FAIL_MESSAGE = 'You lost!'

words = ['python', 'java', 'kotlin', 'javascript']
computer_choice = random.choice(words)
hint = computer_choice[0:3:1] + "-" * (len(computer_choice) - 3)

print(GAME_TITLE)
user_input = str(input(GAME_INPUT_MESSAGE + hint + ": "))

if user_input == computer_choice:
    print(GAME_SUCCESS_MESSAGE)
else:
    print(GAME_FAIL_MESSAGE)
    