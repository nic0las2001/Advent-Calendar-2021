import time
import progressbar

def lanternfish(days):
    open_input = open("d6_input.txt","r")

    read_input_str = open_input.read()
    read_input = read_input_str.split(',')

    count_dict = {}
    new_dict = {}

    for i in range(9):
        count_dict[i] = 0
        new_dict[i] = 0

    for i in range(0,len(read_input)):
        read_input[i] = int(read_input[i])
        if read_input[i] in count_dict:
            count_dict[read_input[i]] += 1
        else:
            count_dict[read_input[i]] = 1

    for i in progressbar.progressbar(range(days)):
        #print(new_dict)
        for entry in count_dict:
            if entry > 0:
                new_dict[entry-1] += int(count_dict[entry])
            else:
                new_dict[6] += int(count_dict[entry])
                new_dict[8] = int(count_dict[entry])
        total_value = 0
        for value in count_dict:
            count_dict[value] = new_dict[value]
            total_value += new_dict[value]
        for z in range(9):
            new_dict[z] = 0

    open_input.close()
    return total_value

#Part 1
print(lanternfish(80))

#Part 2
print(lanternfish(256))
