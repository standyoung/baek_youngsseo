import sys
n, k = map(int, input().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0
for i in range(1, n):
    loc = i - 1  # temp의 왼쪽 인덱스
    newItem = A[i]

    while (0 <= loc) and (newItem < A[loc]):
        A[loc+1] = A[loc]
        ans = A[loc+1]
        loc -= 1
        cnt += 1
        # print("A1 : ", A)
        # print("cnt : ", cnt)
        # print(ans)
        if cnt == k:
            print(ans)
            break

    if loc+1 != i:
        A[loc+1] = newItem
        ans = A[loc+1]
        cnt += 1
        # print("A2 : ", A)
        # print("cnt : ", cnt)
        # print(ans)

        if cnt == k:
            print(ans)
            break

if cnt < k:
    print(-1)
