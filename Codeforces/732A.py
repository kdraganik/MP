k, r = [int(i) for i in input().split()]

numOfShovels = 1

while k * numOfShovels % 10 != 0 and k * numOfShovels % 10 != r:
    numOfShovels += 1

print(numOfShovels)