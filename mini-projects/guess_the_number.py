# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import math
import simplegui
import random

# initialize global variables used in your code

num_range = 100
tries = 7
random_choice = 0

# helper function to start and restart the game

def assign_random_number(range):
    """ Returns a random integer inside range """
    return random.randint(0, range - 1)

def new_game():
    global num_range, tries, random_choice
    
    random_choice = assign_random_number(num_range)
    
    if num_range != 100:
        tries = 10
    else:
        tries = 7
        
    print "New game started (range is from 0 to " + str(num_range) + ")"
    print "You have " + str(tries) + " tries left"
    
def range100():
    global num_range
    num_range = 100
    print "\n"
    new_game()

def range1000():
    global num_range
    num_range = 1000
    print "\n"
    new_game()
    
def input_guess(guess):
    global tries
    int_guess = int(guess)
    print "\nYour guess is " + guess
    
    if int_guess > random_choice:
        print "Lower!"
    elif int_guess < random_choice:
        print "Higher!"
    else:
        print "Great job! Number found!\n"
        return new_game()
    
    tries = tries - 1
    if tries < 1:
        print "Nope. Start again.\n"
        return new_game()
    else:
        print "You have " + str(tries) + " tries left."

# creates the frame        
        
frame_game = simplegui.create_frame("Guess the number", 200, 200)
frame_game.add_button("Range [0, 10]", range100, 200)
frame_game.add_button("Range [0, 1000]", range1000, 200)
frame_game.add_input("Make a guess", input_guess, 200)

# starts a new game

new_game()
