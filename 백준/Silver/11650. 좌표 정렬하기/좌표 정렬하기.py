import sys
n = int(input())
lst = [0]*n

for i in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    lst[i] = [x, y]

lst.sort()

for i in range(n):
    print(*lst[i], sep=" ")