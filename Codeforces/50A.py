N, M = [int(x) for x in input().split()]

if N % 2 == 0:
    print(int(M * N / 2))
else:
    print(int(M * (N - 1) / 2 + M // 2))