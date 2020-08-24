# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

range=100
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, guesses
    secret_number=random.randrange(0, range)
    guesses=int(math.ceil(math.log(range,2)))
    print "New game. Range is [0,"+str(range)+")"
    print "Number of remaining guesses is "+str(guesses)
    print ""


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range
    range=100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range
    range=1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global guesses
    nguess= int(guess)
    guesses-=1
    print "Guess was "+guess
    print "Number of remaining guesses is "+str(guesses)
    if(nguess<secret_number):
        print ("You ran out of guesses.  The number was "+str(secret_number)) if guesses==0 else ("Higher!")
        print ""
        if(guesses==0):
            new_game()
    elif(nguess>secret_number):
        print ("You ran out of guesses.  The number was "+str(secret_number)) if guesses==0 else ("Lower!")
        print ""
        if(guesses==0):
            new_game()
    elif(nguess==secret_number):
        print "Correct!"
        print ""
        new_game()

    
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)
button1 = frame.add_button("Range is [0,100)", range100,200)
button2 = frame.add_button("Range is [0,1000)", range1000,200)
inp = frame.add_input('Enter a guess', input_guess, 200)



# register event handlers for control elements and start frame


frame.start()
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
