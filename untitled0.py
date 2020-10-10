#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:55:47 2020

@author: Leigh Menendez, Devon Milley, Joey Epstein
"""

# This is where we are importing the two libraries that will be used in our code. The random library will allow the program to choose a random word from a set of words. The emoji library allows us to insert emojis into the program.
def hangman():
    import random
# To install emoji into spyder you need to first open the “anaconda prompt” on your computer. Type in “pip install emoji --upgrade” and press enter. If you don't use spyder, open your computer's command prompt and type in “pip install emoji --upgrade”.
    import emoji

# This code asks the user for their name and provides an introduction and summary of the rules.

    player = input('Hello! What is your name?: ')
    print('\nHello', player + '!', 'Welcome to Hangman! Lets go over the rules.')
    print('\nThe rules for this game are simple. You will type in ONE letter to guess each time. You may only guess letters (NO NUMBERS OR SYMBOLS). If your guess is right, it will appear in the correct spot in the word. However, if you guess wrong then you will lose a "life". You have a total of 5 lives. The goal is to guess the word before running out of lives.')
    print('\nLets get started!')

# This code is the list of words that the random library will choose from when picking a word that the user will guess

    words = ('lion', 'cow', 'pig', 'wolf', 'panda', 'kangaroo', 'alligator', 'chipmunk', 'owl', 'rhino', 'dog', 'cat', 'tiger', 'fish', 'dolphin', 'whale', 'hamster', 'parrot', 'otter', 'crocodile', 'hippo', 'giraffe', 'horse', 'monkey', 'sheep', 'ostrich', 'elephant', 'zebra', 'squirrel', 'deer', 'reindeer', 'turkey', 'chicken', 'bird', 'snake', 'camel', 'duck', 'fox', 'cheetah', 'porcupine', 'crab')

# This code chooses the random word that the user will guess

    word = random.choice(words)  

# This code initializes the guess variable

    guess = (' ')

# this is the code for the total number of lives the user has. The number of lives decreases only when they guess wrong, not every time they guess.

    total_lives = 6
    

# This section involves code for beginning our game’s while loop, formats the dashes of the letters so that every time a correct letter is guessed, the letter replaces the dash, and involves the code for guessing the right letter and winning the game
# guessed is a list that keeps track of which letter the user has already guessed.
    guessed = list()
    while total_lives > 0:
        count = 0
        for letter in word:
        # this if statement prints the letter in place of the dash
            if letter in guess:
                print(letter, end = ' ') 
        # this else statement below prints the dash again when the guess is wrong   
            else:
                print("__", end = ' ')
                count = count + 1
    
# This if statement below prints the winning statement after all the dashes are filled which is why we include the count == 0. The emojize method adds three smirking face emojis from the emoji library we imported at the beginning of the code 
            if count == 0:
                print('\nYou won!', (emoji.emojize(":smirking_face:")) * 3,  'The word was', word + '.')
                break
 
# This section involves the code where the user’s guesses are inputted, and all potential errors that could occur in our game are addressed and fixed
    # pick is the user's input of a letter
        pick = input('Guess a letter: ')
    # pick.strip gets rid of blank space on either side of the user's guess
        pick = pick.strip()
    # pick.lower makes all guesses lowercase so that it doesn't have to check both uppercase and lowercase letters
        pick = pick.lower()
    # This code below checks the user's input to make sure it's in the alphabet. If it's not, it returns a message telling the user to avoid numbers or symbols.
        if not pick.isalpha():
            print('Only use letters! No numbers, special characters or symbols.')
            continue
    # This code below makes sure that the user only inputs one letter at a time. If the user inputs multiple letters, it returns a message telling the user that only one letter can be guessed at a time
        elif len(pick) > 1:
            print('Only one letter can be guessed each turn.')
            continue
    # This code below checks the list of letters already guessed to make sure they don't guess the same letter twice. If the letter is already in the list of guessed letters, the code returns a message telling the user they've already guessed that letter.
        elif pick in guessed:
            print('You have already guessed that letter.')
            continue

# This section involves the code for our ‘guess box,’ which will show the user what letters they have guessed for reference during the game
    # The append method adds any guess the user inputs into the guessed list
        guessed.append(pick)
    # After each time the user guesses a letter, the code prints out the guess box of letters for their easy viewing
        print("Guess box: " + str(guessed))

# This section involves the code for what happens if you guess the wrong letter and lose the game. 
    # This code below says that if the user's guess is incorrect, it subtracts one from their total lives. After each time they lose a life, a body part is added to the hangman, and the user is told how many lives they have left.

        if pick not in word:
            total_lives = total_lives - 1
            if total_lives == 5:
                print('Your hangman now has a Head.', '\nYou have', total_lives, 'lives left.')
                if total_lives == 4:
                    print('Your hangman now has a Body.', '\nYou have', total_lives, 'lives left.')
# when the user has three lives left, they are given a hint that the word is an animal
            if total_lives == 3:
                print('Your hangman now has one Arm now.', 'Hint: It is an animal', '\nYou have', total_lives, 'lives left.')
            if total_lives == 2:
                print('Your hangman now has both Arms now.', '\nYou have', total_lives, 'lives left.')
# when the user has one life left, they are told to take their time with their (possible) last guess
            if total_lives == 1:
                print('Your hangman now has one Leg.', '\nYou only have', total_lives, 'life left! Take your time with this last guess!')
#Once the total lives is zero, the user sees a message that says they lost the game. The emojize methods adds three crying face emojis from the emoji list we imported at the beginning of the code
            if total_lives == 0:
                print('\nYour hangman is hung', (emoji.emojize(':crying_face:')) * 3, 'Game Over! Better luck next time. The word was', word + '.')
# This code saves the user's previous guesses and adds the new pick each time until the word is complete which allows you to win the game
        guess = guess + pick
        
hangman()




