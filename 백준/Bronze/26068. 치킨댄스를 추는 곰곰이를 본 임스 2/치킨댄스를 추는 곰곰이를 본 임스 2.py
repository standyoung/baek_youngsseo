n = int(input())
cnt = 0
for _ in range(n):
    d = input()
    d = int(d[2:])

    if d <= 90:
        cnt += 1
print(cnt)
