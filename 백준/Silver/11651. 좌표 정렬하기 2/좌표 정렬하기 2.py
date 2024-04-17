import sys
n = int(sys.stdin.readline().rstrip())
lst = [[0, 0] for _ in range(n)]

for i in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    lst[i][0] = y
    lst[i][1] = x

lst.sort()

for i in range(n):
    print(lst[i][1], lst[i][0])
