def passwordTest(num):
    hasDouble = False
    isIncreasing = True
    numStr = str(num)
    for i, digit in enumerate(numStr):
        if i + 1 < len(numStr):
            if (int(digit) > int(numStr[i + 1])):
                isIncreasing = False
            if digit == numStr[i + 1]:
                lowerGood = i - 1 < 0 or numStr[i - 1] != digit
                upperGood = i + 2 >= len(numStr) or numStr[i + 2] != digit
                if hasDouble:
                    continue
                hasDouble = lowerGood and upperGood
    return isIncreasing and hasDouble

passwordCount = 0
lower = 387638
higher = 919123

for i in range(lower, higher + 1):
    if passwordTest(i):
        passwordCount += 1
print(passwordCount)
