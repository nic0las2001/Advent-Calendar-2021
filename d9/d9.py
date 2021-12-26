import numpy as np
open_file = open("d9_input.txt","r")

read_file_str = open_file.readlines()
read_file = []

#Convert to a list of numerical lines
for line in read_file_str:
    digits = [int(digit) for digit in line if digit.isnumeric()]
    read_file.append(digits)


def check_func(target,neighbour):
    if target >= neighbour:
        return False
    else:
        return True

droughs = []
(top, bottom, left, right) = (True, True, True, True)
#Iterate through the lines and columns
for i in range(0,len(read_file)): #lines
    for j in range(0,len(read_file[i])): #columns
        (top, bottom, left, right) = (True, True, True, True)
        #Left check
        if j>0:
            left = check_func(read_file[i][j],read_file[i][j-1])
        #Right check
        if j<len(read_file[i])-1:
            right = check_func(read_file[i][j],read_file[i][j+1])
        #Top check
        if i>0:
            top = check_func(read_file[i][j],read_file[i-1][j])
        #Bottom check
        if i<len(read_file)-1:
            bottom = check_func(read_file[i][j],read_file[i+1][j])

        if left and right and top and bottom:
            droughs.append(read_file[i][j])
            #print(i,j)

risk_level = sum(droughs) + len(droughs)
print(risk_level)

#Part 2
def scan_func(file2,i,j,k):
    basin_size = 1
    (left, right, top, bottom) = (0, 0, 0, 0)
    #Set value as 9
    if k == 1:
        file2[i][j] = -1
    else:
        file2[i][j] = 9
    block = [9,-1]
    #Left check
    if j>0:
        if file2[i][j-1] not in block:
            (left, file2) = scan_func(file2,i,j-1,k)
    #Right check
    if j<len(file2[i])-1:
        if file2[i][j+1] not in block:
            (right, file2) = scan_func(file2,i,j+1,k)
    #Top check
    if i>0:
        if file2[i-1][j] not in block:
            (top, file2) = scan_func(file2,i-1,j,k)
    #Bottom check
    if i<len(file2)-1:
        if file2[i+1][j] not in block:
            (bottom, file2) = scan_func(file2,i+1,j,k)
    basin_size += left + right + top + bottom
    return basin_size, file2


#Iterate through the lines and columns
file2 = list(read_file)
#file2 = file2.reshape([100,100])
size_list = []
k = 0
block = [9,-1]
for i in range(0,len(file2)): #lines
    for j in range(0,len(file2[i])): #columns
        k += 1
        if file2[i][j] not in block:
            (basin_size, file2) = scan_func(file2,i,j,k)
            size_list.append(basin_size)
size_list.sort()
l = len(size_list)
(top1, top2, top3) = (size_list[l-1],size_list[l-2],size_list[l-3])
multiply = top1*top2*top3
print(top1,top2,top3,multiply)
