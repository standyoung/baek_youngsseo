n = int(input())
cnt = 0
for _ in range(n):
    h, v = map(int, input().split())
    if h == 136:
        cnt += 1000
    elif h == 142:
        cnt += 5000
    elif h == 148:
        cnt += 10000
    elif h == 154:
        cnt += 50000

print(cnt)
