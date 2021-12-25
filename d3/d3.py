open_input = open("d3_input.txt","r")

read_input = open_input.read()
input_list = read_input.split()

zero_count = []
one_count = []
relevant_oxygen = []

#Create counter for digit
for letter in input_list[0]:
    zero_count.append(0)
    one_count.append(0)
    relevant_oxygen.append([])

relevant_oxygen[0] = input_list
relevant_carbon = list(relevant_oxygen)

#Counting each digit
for element in input_list:
    for i in range(0,len(element)):
        if element[i] == '1':
            one_count[i] += 1
        else:
            zero_count[i] += 1

#Comparing values
gamma = ''
epsilon = ''
for i in range(0,len(zero_count)):
    if one_count[i] > zero_count[i]:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

#Binary to decimal
power_consumption = int(gamma, 2)*int(epsilon, 2)

print(gamma, epsilon, power_consumption)


#Part 2
oxy = ''
carb = ''
for i in range(0,len(relevant_oxygen)):
    one_count_o = 0
    zero_count_o = 0
    one_count_c = 0
    zero_count_c = 0
    ox_o = []
    ox_z = []
    carb_o = []
    carb_z = []
    if len(relevant_oxygen[i]) == 1:
        oxy = relevant_oxygen[i][0]
        if i<len(relevant_carbon)-1:
            relevant_oxygen[i+1] = relevant_oxygen[i]
    else:
        for value in relevant_oxygen[i]:
            if value[i] == '1':
                one_count_o += 1
                ox_o.append(value)
            else:
                zero_count_o += 1
                ox_z.append(value)
        if one_count_o > zero_count_o:
            oxy += '1'
            if i<len(relevant_oxygen)-1:
                relevant_oxygen[i+1] = ox_o
        elif one_count_o == zero_count_o:
            oxy += '1'
            if i<len(relevant_oxygen)-1:
                relevant_oxygen[i+1] = ox_o
        else:
            oxy += '0'
            if i<len(relevant_oxygen)-1:
                relevant_oxygen[i+1] = ox_z
    if len(relevant_carbon[i]) == 1:
        carb = relevant_carbon[i][0]
        if i<len(relevant_carbon)-1:
            relevant_carbon[i+1] = relevant_carbon[i]
    else:
        for value in relevant_carbon[i]:
            if value[i] == '1':
                one_count_c += 1
                carb_o.append(value)
            else:
                zero_count_c += 1
                carb_z.append(value)
        if one_count_c > zero_count_c:
            carb += '0'
            if i<len(relevant_oxygen)-1:
                relevant_carbon[i+1] = carb_z
        elif one_count_c == zero_count_c:
            carb += '0'
            if i<len(relevant_oxygen)-1:
                relevant_carbon[i+1] = carb_z
        else:
            carb += '1'
            if i<len(relevant_oxygen)-1:
                relevant_carbon[i+1] = carb_o

#Binary to decimal
life_support = int(oxy, 2)*int(carb, 2)

print(oxy, carb, life_support)
