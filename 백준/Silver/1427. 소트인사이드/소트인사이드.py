import sys

n = sys.stdin.readline().strip()
n = sorted(n, reverse=True)
print(*n, sep="")
