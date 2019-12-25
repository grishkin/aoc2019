with open("./day6/input.txt") as f:
    data = f.readlines()


# total = 0
# orbits = {}
# for line in data:
#     [a, b] = line.split(')')
#     print(a, b)
#     if a in orbits:
#         orbits[b] = orbits[a] + 1
#         total += orbits[b]
#     else:
#         orbits[a] = 0
#         orbits[b] = 1
#         total += 1
# print(total)

orbits = {}
for line in data:
    [a, b] = [x.strip() for x in line.split(')')]
    if b not in orbits:
        orbits[b] = a

youPath = []
currPlanet = 'YOU'
while currPlanet in orbits:
    currPlanet = orbits[currPlanet]
    youPath.append(currPlanet)

sanPath = []
currPlanet = 'SAN'
while currPlanet in orbits:
    currPlanet = orbits[currPlanet]
    sanPath.append(currPlanet)

print(sanPath)

total = 0
for p in youPath:
    total += 1
    print(p)
    if p in sanPath:
        break


for p in sanPath:
    total += 1
    print(p)
    if p in youPath:
        break
print(total)

# total = 0
# for satellite in orbits.keys():
#     currPlanet = orbits[satellite]
#     total += 1
#     while currPlanet in orbits:
#         total += 1
#         currPlanet = orbits[currPlanet]
# print(total)


