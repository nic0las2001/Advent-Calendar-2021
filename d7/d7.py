import numpy as np

def fuel_consumption(median,read_input):
    total_fuel = 0
    for value in read_input:
        total_fuel += abs(median - value)
    return total_fuel

open_input = open("d7_input.txt","r")

read_input_str = open_input.read()
read_input = read_input_str.split(',')

for i in range(0,len(read_input)):
    read_input[i] = int(read_input[i])

read_input.sort()

median = round(np.median(read_input))

#Part 1
print(fuel_consumption(median,read_input))
