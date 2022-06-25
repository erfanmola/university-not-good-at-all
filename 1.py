# Author: Erfan Mola
# I'm not a Python God, Don't expect the best practice
# Thanks to StackOverflow (:

import os, time

size = 12;
positions = [];
animation_interval = 0.025;

def RenderBoard(horse_position = [0,0]):
    
    ClearScreen();

    print("╔═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╗");

    for j in range(0,size):

        str = "║";

        for i in range(0,size):
            
            if (horse_position[0] == i and j == horse_position[1]):

                str += "♞║";
            
            elif ([i, j] in positions) :

                str += "♘║";

            else:
                
                str += " ║";

        print(str);
        
        if (j == (size-1)):

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

        board[key] = [item[0], abs(item[1] - (size-1))];

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

            data = [int(string[0]), int(string[1])];

            if (data[0] < size and data[1] < size):

                return data;

    GetInput();

# -----------------------------------------

def SolveTheMysteriousPuzzleThatUniversityAskedUsToSolveAndItsCompletelyUselessScenarioInRealLifeButIHaveToSolveItToPass(data):

    temp_data = data[:];
    last_pos  = data[-1];
    
    if (len(temp_data) == (size*size)):

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

    global size;

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

    if ((x > (size-1) or x < 0) or (y > (size-1) or y < 0)):

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