import sys

n = int(sys.stdin.readline())

s = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().split()))

for i in range(len(l)):
    if l[i] in s:
        print(1)
    else:
        print(0)
