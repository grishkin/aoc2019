import itertools

with open("./day7/input.txt") as f:
    data = f.read()

# only 5 amplifiers
# 0 - 4

def get_output(codes_pos, phase, inp):
    codes = [int(x) for x in data.split(',')]
    [codes, curr_pos, is_first] = codes_pos

    while codes[curr_pos] != 99:
        op = str(codes[curr_pos]).zfill(5)
        op_code = int(op[3:])
        first_mode = int(op[2:3])
        second_mode = int(op[1:2])
        # third_mode = int(op[:1])

        if op_code == 1 or op_code == 2:
            p1 = codes[curr_pos + 1] if first_mode else codes[codes[curr_pos + 1]]
            p2 = codes[curr_pos + 2] if second_mode else codes[codes[curr_pos + 2]]
            if op_code == 1:
                x = p1 + p2

            if op_code == 2:
                x = p1 * p2

            codes[codes[curr_pos + 3]] = x
            curr_pos += 4

        if op_code == 3 or op_code == 4:
            p1 = codes[curr_pos + 1]

            if op_code == 3:
                if is_first:
                    is_first = False
                    codes[p1] = phase
                    print('is first')
                else:
                    print('taking input')
                    codes[p1] = inp
            if op_code == 4:
                p1 = codes[curr_pos + 1] if first_mode else codes[codes[curr_pos + 1]]
                codes_pos[1] = curr_pos + 2
                codes_pos[0] = codes
                print('outputting')
                return p1
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
    return None

def init_codes():
    return [int(x) for x in data.split(',')]

all_perms = itertools.permutations([5, 6, 7, 8, 9], 5)
max_signal = 0
max_perm = None

for perm in all_perms:
    # instantiate codes for each amplifier
    all_codes = [[init_codes(), 0, True] for i in range(0, 5)]
    inp = 0
    curr_amp = 0
    result = 0
    while True:
        curr_amp = curr_amp % 5
        # run the codes until we get an output
        result = get_output(all_codes[curr_amp], perm[curr_amp], inp)
        all_codes[curr_amp][2] = False

        if curr_amp == 4:
            #print(result)
            if result == None:
                break
            if result > max_signal:
                max_signal = result
                max_perm = perm
        # print(result

        inp = result
        curr_amp += 1


    # print(perm)
    # curr_input = 0
    # for phase in perm:
    #     next_input = get_output(phase, curr_input)
    #     curr_input = next_input
    # if (curr_input > max_signal):
    #     max_signal = curr_input
print(max_signal, max_perm)

