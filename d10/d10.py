from numpy import median
open_file = open("d10_input.txt","r")

read_file = open_file.readlines()

#Remove \n from each line
for i in range(0,len(read_file)):
    read_file[i] = read_file[i][0:len(read_file[i])-1]

symbol_matches = {'(':')','{':'}','[':']','<':'>'}
error_points = {')':3,'}':1197,']':57,'>':25137}
error_balance = 0
non_corrupted = []
completed_sentences = []
for line in read_file:
    expected = []
    corrupted = False
    for character in line:
        if character in symbol_matches:
            expected.insert(0,symbol_matches[character])
        else:
            if character == expected[0]:
                discarded = expected.pop(0)
            else:
                error_balance += error_points[character]
                corrupted = True
                break
    if corrupted == False:
        completed_sentences.append(list(expected))
        non_corrupted.append(str(line))

#Part 1
print(error_balance)

#Part 2
complete_points = {')':1,'}':3,']':2,'>':4}
complete_balances = []

for sequence in completed_sentences:
    seq_bal = 0
    for item in sequence:
        seq_bal *= 5
        seq_bal += complete_points[item]
    complete_balances.append(seq_bal)

complete_balances.sort()
print(median(complete_balances))
