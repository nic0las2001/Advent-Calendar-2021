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
