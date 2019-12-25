with open("./day2/input.txt") as f:
    data = f.read()

def get_output(noun, verb):
    codes = [int(x) for x in data.split(',')]
    codes[1] = noun
    codes[2] = verb

    currPos = 0

    while codes[currPos] != 99:
        x = codes[codes[currPos + 1]]
        y = codes[codes[currPos + 2]]

        if codes[currPos] == 1:
            result = x + y

        if codes[currPos] == 2:
            result = x * y

        codes[codes[currPos + 3]] = result
        currPos += 4

    return codes[0]


goal = 19690720
input_lower = 0
input_upper = 99

for i in range(input_lower, input_upper + 1):
    for j in range(input_lower, input_upper + 1):
        if get_output(i, j) == goal:
            print(i, j)
            break