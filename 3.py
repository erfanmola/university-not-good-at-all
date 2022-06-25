# Author: Erfan Mola
# I'm not a Python God, Don't expect the best practice
# Thanks to StackOverflow (:

import os

words = [ 'hate', 'university', 'waste', 'time' ];

def ClearScreen():

    os.system('cls' if os.name=='nt' else 'clear')

# -----------------------------------------

def Start():
    
    ClearScreen();


# -----------------------------------------

if __name__ == "__main__":

    Start();