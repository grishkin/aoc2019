with open("./day5/input.txt") as f:
    data = f.read()


codes = [int(x) for x in data.split(',')]
curr_pos = 0
result = 0

while codes[curr_pos] != 99:
    op = str(codes[curr_pos]).zfill(5)
    op_code = int(op[3:])
    first_mode = int(op[2:3])
    second_mode = int(op[1:2])
    third_mode = int(op[:1])

    if op_code == 1 or op_code == 2:
        p1 = codes[curr_pos + 1] if first_mode else codes[codes[curr_pos + 1]]
        p2 = codes[curr_pos + 2] if second_mode else codes[codes[curr_pos + 2]]
        if op_code == 1:
            result = p1 + p2

        if op_code == 2:
            result = p1 * p2

        codes[codes[curr_pos + 3]] = result
        curr_pos += 4

    if op_code == 3 or op_code == 4:
        p1 = codes[curr_pos + 1]

        if op_code == 3:
            codes[p1] = 5
        if op_code == 4:
            p1 = codes[curr_pos + 1] if first_mode else codes[codes[curr_pos + 1]]
            print(p1)
        curr_pos += 2

    if op_code == 5:
        p1 = codes[curr_pos + 1] if first_mode else codes[codes[curr_pos + 1]]
        p2 = codes[curr_pos + 2] if second_mode else codes[codes[curr_pos + 2]]
        if p1 != 0:
            curr_pos = p2
        else:
            curr_pos += 3
    
    if op_code == 6:
        p1 = codes[curr_pos + 1] if first_mode else codes[codes[curr_pos + 1]]
        p2 = codes[curr_pos + 2] if second_mode else codes[codes[curr_pos + 2]]
        if p1 == 0:
            curr_pos = p2
        else:
            curr_pos += 3

    if op_code == 7 or op_code == 8:
        p1 = codes[curr_pos + 1] if first_mode else codes[codes[curr_pos + 1]]
        p2 = codes[curr_pos + 2] if second_mode else codes[codes[curr_pos + 2]]
            
        if op_code == 7:
            codes[codes[curr_pos + 3]] = 1 if p1 < p2 else 0
            
        if op_code == 8:
            codes[codes[curr_pos + 3]] = 1 if p1 == p2 else 0

        curr_pos += 4