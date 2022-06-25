# Author: Erfan Mola
# I'm not a Python God, Don't expect the best practice
# Thanks to StackOverflow (:

import os, time

from more_itertools import last

positions = [];
animation_interval = 0.25;

def RenderBoard(horse_position = [0,0]):
    
    ClearScreen();

    print("╔═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╗");

    for j in range(0,12):

        str = "║";

        for i in range(0,12):
            
            if (horse_position[0] == i and j == horse_position[1]):

                str += "♞║";
            
            elif ([i, j] in positions) :

                str += "♘║";

            else:
                
                str += " ║";

        print(str);
        
        if (j == 11):

            print("╚═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╝");

        else:

            print("╠═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╬═╣");

# -----------------------------------------

def AnimateSolution(solution):

    solution = ReverseChessBoard(solution);

    for item in solution:

        RenderBoard(item);
        positions.append(item);
        time.sleep(animation_interval);

# -----------------------------------------

def ReverseChessBoard(board):

    for (key, item) in enumerate(board):

        board[key] = [item[0], abs(item[1] - 11)];

    return board;

# -----------------------------------------

def ClearScreen():

    os.system('cls' if os.name=='nt' else 'clear')

# -----------------------------------------

def GetInput():

    string = input('Please enter a valid starting point (example: 0,0) : ');

    if (string.find(',')) :
        
        string = string.split(',');

        if (len(string) == 2) :

            return [int(string[0]), int(string[1])];

    GetInput();

# -----------------------------------------

def SolveTheMysteriousPuzzleThatUniversityAskedUsToSolveAndItsCompletelyUselessScenarioInRealLifeButIHaveToSolveItToPass(data):

    temp_data = data[:];
    last_pos  = data[-1];
    
    if (len(temp_data) == 144):

        return temp_data;

    for i in range(8):
        
        move_position = CalculateLMovement(last_pos[0], last_pos[1], i);

        if move_position != None and move_position not in temp_data:

            temp_data.append(move_position);
            new_data = SolveTheMysteriousPuzzleThatUniversityAskedUsToSolveAndItsCompletelyUselessScenarioInRealLifeButIHaveToSolveItToPass(temp_data);

            if (new_data != None) :

                    return new_data;
    
    return None;

# -----------------------------------------

def CalculateLMovement(x, y, type = 0):

    if (type == 0) :

        x += 2;
        y += 1;

    elif (type == 1) :

        x += 2;
        y -= 1;

    elif (type == 2) :

        x -= 2;
        y += 1;

    elif (type == 3) :

        x -= 2;
        y -= 1;

    elif (type == 4) :

        x -= 1;
        y += 2;

    elif (type == 5) :

        x -= 1;
        y -= 2;

    elif (type == 6) :

        x += 1;
        y += 2;

    elif (type == 7) :

        x += 1;
        y -= 2;

    else :

        return None;

    if ((x > 11 or x < 0) or (y > 11 or y < 0)):

        return None;

    else:
        
        return [x, y]

# -----------------------------------------

def Start():

    data = GetInput();

    ClearScreen();
    print('\n\nProcessing the solution ...\n\n');

    solution = SolveTheMysteriousPuzzleThatUniversityAskedUsToSolveAndItsCompletelyUselessScenarioInRealLifeButIHaveToSolveItToPass([ data ]);

    AnimateSolution(solution);

if __name__ == "__main__":
    
    Start();