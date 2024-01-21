import sys
t = int(input())

for _ in range(t):
    n = list(map(int, sys.stdin.readline().rstrip().split()))
    n.sort()

    if max(n[1:4]) - min(n[1:4]) >= 4:
        print("KIN")
    else:
        print(sum(n[1:4]))
