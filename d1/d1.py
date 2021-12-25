open_input = open("d1_input.txt","r")

read_input = open_input.read()
input_list = read_input.split()
numeric_input = []
[numeric_input.append(int(item)) for item in input_list]

increases = 0
for i in range(1,len(numeric_input)):
    if numeric_input[i] > numeric_input[i-1]:
        increases += 1

print(increases)

#Part 2
sum_trio = []
for i in range(0,len(numeric_input)-2):
    sum_trio.append(numeric_input[i] + numeric_input[i+1] + numeric_input[i+2])

increases = 0
for j in range(1,len(sum_trio)):
    if sum_trio[j] > sum_trio[j-1]:
        increases += 1

print(increases)
