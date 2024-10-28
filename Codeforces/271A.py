def czyTeSameCyfry(rok):
    rok = str(rok)
    cyfry = [c for c in rok]
    for i in range(1, len(cyfry)):
        for j in range(i):
            if cyfry[i] == cyfry[j]:
                return True
    return False

y = int(input()) + 1
while czyTeSameCyfry(y):
    y += 1

print(y)