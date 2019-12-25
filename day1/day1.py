import math

with open("./day1/input.txt") as f:
    data = f.readlines()

result = 0

for massStr in data:
    mass = int(massStr)
    fuel = math.floor(mass / 3) - 2

    while fuel > 0:
        result += fuel
        fuel = math.floor(fuel / 3) - 2

print(result)