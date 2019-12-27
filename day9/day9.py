with open("./day9/input.txt") as f:
    data = f.read()

extra_mem = {}
codes = [int(x) for x in data.split(',')]

def get_codes(loc):
    if loc > len(codes) - 1:
        if loc not in extra_mem:
            extra_mem[loc] = 0
        return extra_mem[loc]
    return codes[loc]

def set_codes(loc, val):
    if loc > len(codes) - 1:
        extra_mem[loc] = val
    else:
        codes[loc] = val 


def param_with_mode(codes, p, mode, rel_pos):
    if mode == 0:
        #print('mode 0', p, codes[p])
        return get_codes(get_codes(p))
    elif mode == 1:
        return get_codes(p)
    elif mode == 2:
        return get_codes(rel_pos + get_codes(p))

def get_params(op, rel_pos, curr_pos, codes):
    op_code = int(op[3:])
    first_mode = int(op[2:3])
    second_mode = int(op[1:2])
    third_mode = int(op[0:1])

    # p1 = 0
    # p2 = 0

    # if op_code in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    p1 = param_with_mode(codes, curr_pos + 1, first_mode, rel_pos)
    if op_code == 3:
        print(first_mode)
    #if op_code == 3:
    #    print('HERE', op_code, 'mode', first_mode, 'param result', p1, 'relpos', rel_pos,'first param', get_codes(curr_pos + 1))
    #if op_code != 4 and op_code != 9:
    p2 = param_with_mode(codes, curr_pos + 2, second_mode, rel_pos)
    p3 = param_with_mode(codes, curr_pos + 3, third_mode, rel_pos)

    # elif op_code == 3:
     #   p1 = get_codes(curr_pos + 1)
    return (op_code, p1, p2, p3)

curr_pos = 0
rel_pos = 0
result = 0
first_inp = True

while get_codes(curr_pos) != 99:
    op = str(get_codes(curr_pos)).zfill(5)
    (op_code, p1, p2, p3) = get_params(op, rel_pos, curr_pos, codes)
    # print(op_code)

    if op_code == 1:
        set_codes(get_codes(curr_pos + 3), p1 + p2)
        curr_pos += 4

    if op_code == 2:
        set_codes(get_codes(curr_pos + 3), p1 * p2)
        curr_pos += 4

    if op_code == 3:
        # print('set', p1, p2)
        # # if first_inp:
        # print('before', get_codes(1000))
        # print('before', get_codes(3))

        set_codes(p1,  1)
        # print('after', get_codes(1000))
        # print('before', get_codes(3))

        #first_inp = False
        # else:
        #     # todo remove
        #     print('?')
        #     set_codes(p1, p2)
        curr_pos += 2

    if op_code == 4:
        curr_pos += 2
        print('output',p1)

    if op_code == 5:
        if p1 != 0:
            curr_pos = p2
        else:
            curr_pos += 3
    
    if op_code == 6:
        if p1 == 0:
            curr_pos = p2
        else:
            curr_pos += 3

    if op_code == 7:
        set_val = 1 if p1 < p2 else 0
        set_codes(get_codes(curr_pos + 3), set_val)
        curr_pos += 4  
          
    if op_code == 8:
        set_val = 1 if p1 == p2 else 0
        set_codes(get_codes(curr_pos + 3), set_val)
        curr_pos += 4

    if op_code == 9:
        rel_pos += p1
        curr_pos += 2
