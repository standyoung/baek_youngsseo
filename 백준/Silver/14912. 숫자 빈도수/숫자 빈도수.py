n, d = map(int, input().split())

d = str(d)

start = 1
cnt = 0

while start<=n:
    cnt += str(start).count(d)

    start += 1

print(cnt)