import sys

while True:
    n = int(input())

    if n == 0:
        break

    lst = []
    for _ in range(n):
        s = sys.stdin.readline().rstrip()
        lst.append([s.lower(), s])

    lst.sort()
    print(lst[0][1])
