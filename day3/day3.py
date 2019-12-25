import math

with open("./day3/input.txt") as f:
    data = f.readlines()

wireMap = {}
cmds1 = data[0].split(',')
cmds2 = data[1].split(',')


path = {}

pos = [0, 0]
steps = 0
for cmd in cmds1:
    direction = cmd[0]
    length = int(cmd[1:])

    for i in range(0, length):
        steps += 1
        if direction == 'L':
            pos[0] -= 1
        if direction == 'U':
            pos[1] += 1
        if direction == 'D':
            pos[1] -= 1
        if direction == 'R':
            pos[0] += 1

        coord = ','.join((str(pos[0]) ,str(pos[1])))
        if coord in path:
            continue
        path[coord] = steps

pos = [0, 0]
minSteps = math.inf
minInt = []
steps = 0
for cmd in cmds2:
    direction = cmd[0]
    length = int(cmd[1:])

    for i in range(0, length):
        steps += 1
        if direction == 'L':
            pos[0] -= 1
        if direction == 'U':
            pos[1] += 1
        if direction == 'D':
            pos[1] -= 1
        if direction == 'R':
            pos[0] += 1

        coordKey = ','.join((str(pos[0]), str(pos[1])))
        if (coordKey) in path:
            currSteps = steps + path[coordKey]
            if currSteps < minSteps:
                minSteps = currSteps
                minInt = pos[:]
print(minSteps)

    






