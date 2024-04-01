s = [input().split() for i in range(10)]
cnt = 0

for i in range(0, 10):  # 0 1 2 3 ... 9
    l = set(s[i])

    if len(l) == 1:
        cnt = 1
        break

if cnt == 0:
    for i in range(0, 10):
        l = set()
        for j in range(0, 10):
            l.add(s[j][i])

        if len(l) == 1:
            cnt = 1
            break

if cnt == 1:
    print(1)

else:
    print(0)
