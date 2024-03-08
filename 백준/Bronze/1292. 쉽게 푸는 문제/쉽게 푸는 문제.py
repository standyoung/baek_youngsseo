a, b = map(int, input().split())
cnt = 0
lst = []
n = 1

while True:
    if cnt == b:
        break

    for i in range(n):
        lst.append(n)

    n += 1
    cnt += 1

print(sum(lst[a-1:b]))
