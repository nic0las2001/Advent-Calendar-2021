import numpy as np

open_input = open("d4_input.txt","r")

read_input = open_input.read()
input_list = read_input.split()

drawn_numbers_txt = input_list.pop(0)
drawn_numbers = drawn_numbers_txt.split(',')

#Part 1
def win_func(grid,number):
    sum_grid = sum(grid)
    grid_reformatted = np.array(grid)
    grid_reformatted = grid_reformatted.reshape([5,5])
    print(grid_reformatted,'\n\n')
    total_score = number*sum_grid
    print(total_score)
    exit()

#Part 2
def lose_func(grid_list,grid,number,blacklist):
    if len(grid_list)>1:
        blacklist.append(grid)
    else:
        win_func(grid,number)
    return blacklist

for i in range(0,len(drawn_numbers)):
    drawn_numbers[i] = int(drawn_numbers[i])

for i in range(0,len(input_list)):
    input_list[i] = int(input_list[i])

blacklist = []
for number in drawn_numbers:
    for i in range(0,len(input_list)):
        if input_list[i] == number:
            input_list[i] = 0

    #Split each of the grids
    grid_list = []
    for element in blacklist:
        for i in range(0,len(element)):
            if element[i] == number:
                element[i] = 0
    for i in range(0,len(input_list),25):
        if list(input_list[i:i+25]) not in blacklist:
            grid_list.append(list(input_list[i:i+25]))

    for grid in grid_list:
        vertical_array = np.array([0,0,0,0,0])
        for i in range(0,len(grid),5):
            it_vector = np.array(grid[i:i+5])
            vertical_array += it_vector
            if sum(grid[i:i+5]) == 0:
                #win_func(grid,number)
                blacklist = lose_func(grid_list,grid,number,blacklist)

        if 0 in vertical_array:
            #win_func(grid,number)
            blacklist = lose_func(grid_list,grid,number,blacklist)
