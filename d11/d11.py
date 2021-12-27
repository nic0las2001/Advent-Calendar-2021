open_file = open("d11_input.txt","r")

read_file_str = open_file.readlines()
read_file = []

def flash_spread(read_file,i,j):
    flash_count = 0
    if read_file[i][j] == 10:
        (a,b,c,d,e,f,g,h) = (0,0,0,0,0,0,0,0)
        read_file[i][j] = 0
        flash_count = 1
        (left, right, top, bottom) = (j>0, j<len(read_file[i])-1, i>0, i<len(read_file)-1)
        #Set value as 0
        block = [10,0]
        #Left check
        if left:
            if read_file[i][j-1] not in block:
                (a, read_file) = flash_spread(read_file,i,j-1)
            if top:
                if read_file[i-1][j-1] not in block:
                    (e, read_file) = flash_spread(read_file,i-1,j-1)
            if bottom:
                if read_file[i+1][j-1] not in block:
                    (f, read_file) = flash_spread(read_file,i+1,j-1)
        #Right check
        if right:
            if read_file[i][j+1] not in block:
                (b, read_file) = flash_spread(read_file,i,j+1)
            if top:
                if read_file[i-1][j+1] not in block:
                    (g, read_file) = flash_spread(read_file,i-1,j-1)
            if bottom:
                if read_file[i+1][j+1] not in block:
                    (h, read_file) = flash_spread(read_file,i+1,j-1)
        #Top check
        if top:
            if read_file[i-1][j] not in block:
                (c, read_file) = flash_spread(read_file,i-1,j)
        #Bottom check
        if bottom:
            if read_file[i+1][j] not in block:
                (d, read_file) = flash_spread(read_file,i+1,j)
        flash_count += int(sum((a,b,c,d,e,f,g,h)))
    else:
        read_file[i][j] += 1
    if read_file[i][j] == 10:
        flash_count = flash_spread(read_file,i,j)
    return flash_count, read_file

for line in read_file_str:
    line_list = []
    for char in line:
        if char not in ['\n']:
            line_list.append(int(char))
    read_file.append(line_list)

total_count = 0
for steps in range(0,100):
    plus_one = [[1]*10]*10
    for i in range(0,10):
        read_file[i] = [a+b for a,b in zip(read_file[i],plus_one[i])]
    for i in range(0,len(read_file)):
        for j in range(0,len(read_file[0])):
            if read_file[i][j] == 10:
                count = flash_spread(read_file,i,j)
                total_count += count
