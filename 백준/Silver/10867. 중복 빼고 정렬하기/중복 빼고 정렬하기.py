import sys

n = int(sys.stdin.readline())

lst = set(map(int, sys.stdin.readline().split()))

lst = list(lst)
lst.sort()

print(*lst, sep=" ")
