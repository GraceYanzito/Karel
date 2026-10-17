import karel


def main():
    """ Function to cause Karel to retrieve the newspaper. """
    move_to_newspaper()
    pick_up_paper()
    return_to_start()


def move_to_newspaper():
    """ Helping function to move Karel to the newspaper location. """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()


def turn_right():
    for i in range(3): turn_left()


def pick_up_paper():
    """ Helping function to have Karel pick up the newspaper. """
    # Yes, this will probably be VERY simple and short
    pick_beeper()
    turn_left()
    turn_left()



def return_to_start():
    """ Helping function to move Karel back to its starting position. """
    for i in range(3):
        move()
    turn_right()
    move()
    turn_right()
