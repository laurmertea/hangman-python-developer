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
