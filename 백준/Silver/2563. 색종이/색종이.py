arr = [[0 for _ in range(100)] for _ in range(100)]

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    x = x - 1
    y = y - 1

    for i in range(10):
        for j in range(10):
            arr[x + i][y + j] += 1
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] >= 1:
            cnt += 1
print(cnt)