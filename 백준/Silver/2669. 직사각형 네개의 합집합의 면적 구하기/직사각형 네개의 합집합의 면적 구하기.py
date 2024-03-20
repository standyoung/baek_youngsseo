lst = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1+1, y2+1):
        for j in range(x1+1, x2+1):
            lst[i][j] = 1

ans = 0
for i in range(101):
    for j in range(101):
        if lst[i][j] == 1:
            ans += 1

print(ans)