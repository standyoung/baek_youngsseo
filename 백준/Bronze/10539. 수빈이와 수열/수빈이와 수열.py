import sys

n = int(input())
summ = 0
a_lst = []

b_lst = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(n):
    if i == 0:
        a_lst.append(b_lst[0])
    else:
        summ = sum(a_lst[:i])
        a_lst.append(b_lst[i]*(i+1)-summ)

print(*a_lst, sep=" ")
