N = int(input())

cnt = 0

for i in range(1, 500):  # B
    for j in range(1, 500):  # A
        if (j**2) == (i**2) + N:
            cnt += 1

print(cnt)