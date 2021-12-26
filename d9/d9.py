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
            print(i,j)

risk_level = sum(droughs) + len(droughs)
print(risk_level)
