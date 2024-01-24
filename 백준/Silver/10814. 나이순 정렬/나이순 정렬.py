import sys
n = int(input())
lst = []

for i in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    lst.append([int(age), i, name])

lst = sorted(lst)

for i in range(n):
    print(lst[i][0], lst[i][2])
