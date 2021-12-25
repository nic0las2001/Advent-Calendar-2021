open_input = open("d6_input.txt","r")

read_input_str = open_input.read()
read_input = read_input_str.split(',')

for i in range(0,len(read_input)):
    read_input[i] = int(read_input[i])

for i in range(80):
    append_list = []
    for j in range(0,len(read_input)):
        if read_input[j] > 0:
            read_input[j] -= 1
        else:
            read_input[j] = 6
            append_list.append(8)
    read_input.extend(append_list)

print(len(read_input))
