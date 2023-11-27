import sys
n, m = map(int, sys.stdin.readline().split())
num = 1

for i in range(n):
    for j in range(m):
        if j != m - 1:
            print(num, end=" ")
        else:
            print(num)
        num += 1
