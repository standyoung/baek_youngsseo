N, M = map(int, input().split())

lst = [0] * N

for _ in range(M):  # M번 공넣기
    i, j, k = map(int, input().split())

    i = i - 1  # 1번 바구니 = 0번 인덱스
    j = j - 1

    for l in range(i, j + 1):
        lst[l] = k

for i in range(len(lst)):
    print(lst[i], end=" ")