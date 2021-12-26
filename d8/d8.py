open_file = open("d8_input.txt","r")

read_file_str = open_file.readlines()
read_input = []
read_output = []
for line in read_file_str:
    line_list = line.split(' | ')
    input_list = line_list[0].split()
    output_list = line_list[1].split()
    read_input.append(list(input_list))
    read_output.append(list(output_list))

pt1_segments_collection = [2,4,3,7] #1 4 7 8

digits_count = 0
for output_list in read_output:
    for code in output_list:
        if len(code) in pt1_segments_collection:
            digits_count += 1
#Part 1
print(digits_count)

#Part 2
segments_dict = {2:'1',4:'4',3:'7',7:'8'}
number_configs = []
total_addition = 0
#Work out the encoding for every line
for input_list in read_input:
    digits_dict = {}
    unidentified = []
    identified = []
    for code in input_list:
        if len(code) in segments_dict:
            digits_dict[segments_dict[len(code)]] = sorted(code)
        else:
            unidentified.append(sorted(code))
    while unidentified != []:
        for item in unidentified:
            if len(item) == 6:
                if all(items in item for items in digits_dict['4']):
                    if '9' not in digits_dict:
                        digits_dict['9'] = item
                elif (not all(items in item for items in digits_dict['1'])):
                    if '6' not in digits_dict:
                        digits_dict['6'] = item
                else:
                    if '0' not in digits_dict:
                        digits_dict['0'] = item
                identified.append(item)
            else:
                if all(items in item for items in digits_dict['1']):
                    if '3' not in digits_dict:
                        digits_dict['3'] = item
                        identified.append(item)
                else:
                    if '9' in digits_dict and all(items in digits_dict['9'] for items in item):
                        if '5' not in digits_dict:
                            digits_dict['5'] = item
                            identified.append(item)
                    elif (len(digits_dict) == 9):
                        digits_dict['2'] = item
                        identified.append(item)
        for item in identified:
            if item in unidentified:
                unidentified.remove(item)
    number_configs.append(dict(digits_dict))

#Decode and sum output
for i in range(0,len(read_output)):
    numerical_code = ""
    for code in read_output[i]:
        val_to_match = sorted(code)
        for key in number_configs[i]:
            if number_configs[i][key] == val_to_match:
                numerical_code += key
                break
    total_addition += int(numerical_code)

print(total_addition)
