import sys
n, k = map(int, input().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0

for i in range(0, n):
    loc = i - 1
    newItem = A[i]

    while (0 <= loc) and (newItem < A[loc]):
        A[loc+1] = A[loc]
        loc -= 1

        cnt += 1
        if cnt == k:
            print(*A, sep=" ")

    if loc+1 != i:
        A[loc+1] = newItem

        cnt += 1
        if cnt == k:
            print(*A, sep=" ")

if cnt < k:
    print(-1)
