n, m = map(int, input().split())
lst = [0 for i in range(0, n+1)]

for i in range(m):
    a, b = map(int, input().split())
    lst[a] += 1
    lst[b] += 1

for i in range(1, n+1):
    print(lst[i])
