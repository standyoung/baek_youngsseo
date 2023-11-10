import sys
K = int(sys.stdin.readline())
lst = []

for i in range(0, K):
    num = int(input())
    if num != 0:
        lst.append(num)
    else:
        lst.pop()

print(sum(lst))
