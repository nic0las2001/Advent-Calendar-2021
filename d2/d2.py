open_input = open("d2_input.txt","r")

read_input = open_input.read()
input_list = read_input.split()

numeric_input = []
for item in input_list:
    try:
        numeric_input.append(int(item))
    except:
        numeric_input.append(item)

depth = 0
position = 0

for i in range(0,len(numeric_input)-1,2):
    if numeric_input[i] == 'forward':
        position += numeric_input[i+1]
    elif numeric_input[i] == 'down':
        depth += numeric_input[i+1]
    elif numeric_input[i] == "up":
        depth -= numeric_input[i+1]

print(depth,position,depth*position)


#Part 2
print('\nPart 2\n')

depth = 0
position = 0
aim = 0

for i in range(0,len(numeric_input)-1,2):
    if numeric_input[i] == 'forward':
        position += numeric_input[i+1]
        depth += aim*numeric_input[i+1]
    elif numeric_input[i] == 'down':
        aim += numeric_input[i+1]
    elif numeric_input[i] == "up":
        aim -= numeric_input[i+1]
print(depth,position,depth*position)
