# Description
# At this stage, you will create a real game, though it will still be quite simple. 
# There will be two possible outcomes. Let's first print a welcome message 
# and then ask the player to guess the word we set for the game. If our player manages to guess the exact word, the game reports "win"; otherwise it will "hang" the player.
# 
# Objectives
# Ask the player for a possible word.
# Print `You survived!` if the user guesses the word.
# Print `You lost!` if the user guesses incorrectly.
# By the way, `python` should be the word the player needs to guess to win the game.
#
# Examples
# The greater-than symbol followed by space (> ) represents the user input. Note that it's not the part of the output.
# Example 1
# H A N G M A N
# Guess the word: > python
# You survived!
#
# Example 2
# H A N G M A N
# Guess the word: > java
# You lost!

GAME_TITLE = 'H A N G M A N'
GAME_INPUT_MESSAGE = 'Guess the word: '
GAME_SUCCESS_MESSAGE = 'You survived!'
GAME_FAIL_MESSAGE = 'You lost!'

print(GAME_TITLE)
user_input = str(input(GAME_INPUT_MESSAGE))

if user_input == 'python':
    print(GAME_SUCCESS_MESSAGE)
else:
    print(GAME_FAIL_MESSAGE)
