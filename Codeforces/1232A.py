t = int(input())
for _ in range(t):
    counter = 0
    a, b = map(int, input().split())
    if a % b == 0:
        print(0)
    else:
        print(b - a % b)