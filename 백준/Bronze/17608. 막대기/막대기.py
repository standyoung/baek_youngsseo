import sys
n = int(input())

lst = [int(sys.stdin.readline().rstrip())for _ in range(n)]

mak_lst = lst[-1]
cnt = 1

rlst = lst[::-1]

for i in range(n):
    if rlst[i] > mak_lst:
        cnt += 1
        mak_lst = rlst[i]

print(cnt)
