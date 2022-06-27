# Author: Erfan Mola
# I'm not a Python God, Don't expect the best practice
# Thanks to StackOverflow (:

import os, string, random

words        = [ "PYTHON", "BORING", "LANGUAGE" ];
grid_size    = 10;
grid         = [ [ '.' for i in range(grid_size) ] for i in range(grid_size) ];
orientations = [ "left-right", "up-down", "diagonal-up", "diagonal-down" ];

# -----------------------------------------

def GenerateGridData():

    try:
        
        global grid;

        grid = [ [ '.' for i in range(grid_size) ] for i in range(grid_size) ];

        for word in words:

            has_placed = False;

            while not has_placed:

                orientation = random.choice(orientations);

                if (orientation == 'left-right'):

                    x_step = 1;
                    y_step = 0;

                elif (orientation == 'up-down'):

                    x_step = 0;
                    y_step = 1;

                elif (orientation == 'diagonal-down'):

                    x_step = 1;
                    y_step = 1;

                elif (orientation == 'diagonal-up'):

                    x_step = 1;
                    y_step = -1;

                x_position = random.randint(0, grid_size);
                y_position = random.randint(0, grid_size);

                x_ending = x_position + len(word) * x_step;
                y_ending = y_position + len(word) * y_step;

                if (x_ending < 0 or x_ending >= grid_size) : continue;
                if (y_ending < 0 or y_ending >= grid_size) : continue;

                failed = False;

                for i in range(len(word)):

                    char = word[i];

                    new_position_x = x_position + i * x_step;
                    new_position_y = y_position + i * y_step;

                    char_at_new_position = grid[new_position_x][new_position_y];

                    if (char_at_new_position != '.') : 
                        if (char_at_new_position == char) : continue;
                        else :
                            failed = True;
                            break;
                
                if (failed) : continue;
                else:
                    for i in range(len(word)):

                        char = word[i];

                        new_position_x = x_position + i * x_step;
                        new_position_y = y_position + i * y_step;

                        grid[new_position_x][new_position_y] = char;
                    
                    has_placed = True;

    except IndexError:

        GenerateGridData();

# -----------------------------------------

def GenerateGridView(populate_with_extra_data = True):
    
    if (populate_with_extra_data) :

        for i in range(grid_size) :

            for j in range(grid_size) :

                if (grid[i][j] == '.') :

                    grid[i][j] = random.choice(string.ascii_uppercase);

    str = '╔' + ('═' * (grid_size * 2)) + '═╗\n';

    for i in range(grid_size):
        
        str += "║ ";
        str += ' '.join(grid[i]);
        str += " ║\n";

    str += '╚' + ('═' * (grid_size * 2)) + '═╝';

    return str;

# -----------------------------------------

def ClearScreen():

    os.system('cls' if os.name=='nt' else 'clear')

# -----------------------------------------

def Start():

    ClearScreen();

    GenerateGridData();

    print(GenerateGridView(False));

    print(GenerateGridView(True));

if __name__ == "__main__":
    
    Start();
