import numpy as np
open_input = open("d5_input.txt","r")

read_input = open_input.read()

#Isolate coordinates
coordinates = []
number = ''
for character in read_input:
    if character.isnumeric():
        number += character
        #print(number,'\n')
    elif number.isnumeric():
        coordinates.append(int(number))
        number = ''

#Generate points and add them to dictionnary
count_points = {}
points_list = []
for i in range(0,len(coordinates),4):
    x = (coordinates[i],coordinates[i+2])
    y = (coordinates[i+1],coordinates[i+3])
    if (coordinates[i] == coordinates[i+2]) or (coordinates[i+1] == coordinates[i+3]):
        for j in range(min(x),max(x)+1): #x coordinates
            for k in range(min(y),max(y)+1): #y coordinates
                points_list.append([j,k])
                entry = str(j) + ' ' + str(k)
                if entry not in count_points:
                    count_points[entry] = 1
                else:
                    count_points[entry] += 1
    #Part 2
    else:
        number_pts = max(x)+1-min(x)
        xs = np.linspace(coordinates[i],coordinates[i+2],number_pts)
        ys = np.linspace(coordinates[i+1],coordinates[i+3],number_pts)
        for j in range(len(xs)):
            x = int(xs[j])
            y = int(ys[j])
            points_list.append([x,y])
            entry = str(x) + ' ' + str(y)
            if entry not in count_points:
                count_points[entry] = 1
            else:
                count_points[entry] += 1

count = 0
for entry in count_points:
    if count_points[entry] >=2:
        count += 1

#open("d5_output.txt","w").write(str(points_list))
print(count)#,len(points_list))
