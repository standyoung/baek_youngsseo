import sys
n, k = map(int, input().split())

A = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0

for last in range(n-1, 0, -1):
    maxInx = A.index(max(A[:last+1]))

    if last != maxInx:
        A[last], A[maxInx] = A[maxInx], A[last]
        cnt += 1

        if cnt == k:
            print(A[maxInx], A[last])
            break

if cnt < k:
    print(-1)