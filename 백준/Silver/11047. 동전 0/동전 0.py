import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

lst = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
lst.sort(reverse=True)

cnt = 0

for i in range(n):  # 4200
    if k >= lst[i]:  # 1000
        cnt += k//lst[i]  # 4
        k = k-lst[i]*(k//lst[i])  # 4200-1000*(4200//1000)
print(cnt)
