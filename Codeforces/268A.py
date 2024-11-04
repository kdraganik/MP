n = int(input())
unifroms = []

for i in range(n):
    unifroms.append(input().split(" "))

counter = 0

for i in range(n):
    for j in range(n):
            if i != j:
                if unifroms[i][0] == unifroms[j][1]:
                    counter += 1

print(counter)