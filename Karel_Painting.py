#====================================================
# Filename: Karel_Painting.py
# 
# Your name: Grace Yanzito
# Who did you work with (if anyone)?: N/A
# If you consulted AI, link to transcript: N/A
# Estimate for time spent on this prob (in hrs)?: 1
#====================================================

# I've just laid out a basic starting function below, but remember that you
# absolutely should define more helping functions to decompose the problem
# into smaller pieces! Here I'm leaving those pieces (and helper functions)
# up to you to design and name as you see fit. Don't forget comments!

import karel

def main():
    """ Function to cause Karel to paint 3 sides of its house and then go indoors. """
    # You can add your code below
    turning()#face the correct direction
    paint_wall()#paint wall 1
    corner()#turn corner
    paint_wall()#paint wall 2
    corner()#turn corner
    paint_wall()#paint wall 3
    corner()#corner
    while left_is_blocked():#gets karel along the different length walls to find the door
        move()
    turn_left()#this and next line get karel into the house through the door
    move()

def turn_right():#turns right instead of having to write it out every time
    turn_left()
    turn_left()
    turn_left()

def turn_180():#turns 180
    turn_left()
    turn_left()

def paint_house():#paints 1/3 of the house and will be repeated 3 times for each wall
    if no_beepers_present():
        put_beeper()
    move()

def paint_wall():
    while left_is_blocked():#this will repeat the painting of an individual wall in order to paint every wall 
        paint_house()#this will paint one individual wall of the house

def corner():#this will turn the corner instead of writing it in full every time
    turn_left()
    move()

def turning():#because each set starts with karel facing a different way this was my solution to getting it to face the correct direction
    if front_is_blocked():
        turn_right()
    if right_is_blocked():
        turn_180()
    if facing_north():
        turn_left()
