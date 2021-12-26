import numpy as np
import progressbar

def fuel_consumption(median,read_input):
    total_fuel = 0
    for value in read_input:
        total_fuel += abs(median - value)
    return total_fuel

def fuel_consumption_pt2(read_input):
    align_value = -1
    total_fuel = 0
    for i in progressbar.progressbar(range(0,max(read_input))):
        value_fuel = 0
        for value in read_input:
            step_fuel = 0
            for j in range(1,abs(i - value)+1):
                step_fuel += j
            value_fuel += step_fuel
        if value_fuel < total_fuel or i == 0:
            total_fuel = value_fuel
            align_value = i
    return 'Fuel used of {} at alignment value {}.'.format(total_fuel, align_value)

open_input = open("d7_input.txt","r")

read_input_str = open_input.read()
read_input = read_input_str.split(',')

for i in range(0,len(read_input)):
    read_input[i] = int(read_input[i])

read_input.sort()

median = round(np.median(read_input))

#Part 1
print(fuel_consumption(median,read_input))

#Part 2
print(fuel_consumption_pt2(read_input))
