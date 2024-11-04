s = input()

count = 0
for i in s:
    if i in ['4', '7']:
        count += 1

if count in [4, 7]:
    print("YES")
else:
    print("NO")