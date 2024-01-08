# 참고코드
import sys

n, k = map(int, input().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))

flag = 0
for last in range(n-1, 0, -1):
    maxNumI = A.index(max(A[:last+1]))

    if last != maxNumI:
        A[last], A[maxNumI] = A[maxNumI], A[last]
        flag += 1

    if flag == k:
        print(*A, sep=" ")
        break

if flag < k:
    print(-1)