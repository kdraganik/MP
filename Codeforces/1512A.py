t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    pattern = 0
    if arr[0] == arr[1]:
        pattern = arr[0]
    elif arr[0] == arr[2]:
        pattern = arr[0]
    elif arr[1] == arr[2]:
        pattern = arr[1]
    for i in range(n):
        if arr[i] != pattern:
            print(i+1)
            break