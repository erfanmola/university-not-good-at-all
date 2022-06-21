# Author: Erfan Mola
# I'm not a Python God, Don't expect a best proctice
# Thanks to StackOverflow (:

import random, time, os

interval = 1000;
score    = 0;
count    = 20;
numbers  = [];
wins     = 0;
total    = 0;

def ShowNumbers():
    
    ClearScreen();

    while (len(numbers) < count):
        
        rand = random.randint(0,99);
        
        if not rand in numbers:

            numbers.append(rand);
        
    print("Score: {}".format(score) + "\n")
    print((', '.join(str(v) for v in numbers)));

# -----------------------------------------

def ProcessAnswer(answer):

    ClearScreen();

    global score, wins, total;

    if (answer == min(numbers)):
        
        score += 10;
        wins += 1;
        
        if (wins == 3):

            print('You Won the game (:');
            exit();
            
        else:

            if (score % 50 == 0):
                
                count += 2;

            if (score % 100 == 0):

                interval -= 50;

    else:

        score -= 2;
        wins = 0;

        print("Oops, Wrong answer, it was {}".format(min(numbers)));

    total += 1;

    time.sleep(1);

    if (total < 10):
        
        Start();

    else:

        print('Game is finished and you Lost :(');
        exit();

# -----------------------------------------

def ClearScreen():

    os.system('cls' if os.name=='nt' else 'clear')

# -----------------------------------------

def Start():
    
    ClearScreen();

    print('Ready ?');
    time.sleep(1);
    ClearScreen();

    print('3');
    time.sleep(1);
    ClearScreen();

    print('2');
    time.sleep(1);
    ClearScreen();

    print('1');
    time.sleep(1);
    ClearScreen();

    ShowNumbers();
    time.sleep(interval / 1000);
    ClearScreen();

    ProcessAnswer(int(input('Guess the Min Value : ')));

# -----------------------------------------

if __name__ == "__main__":

    Start();