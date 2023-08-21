N, M = map(int, input().split())
lst = []

for i in range(N):
    lst.append(i + 1)

num = 0  # 빈 그릇

for _ in range(M):
    i, j = map(int, input().split())  # i,j
    i = i - 1
    j = j - 1

    num = lst[j]  # 사라질 lst[j]는 num에 저장
    lst[j] = lst[i]  # lst[j]에 lst[i]를 대입
    lst[i] = num

# lst = [3, 1, 4, 2, 5]
for i in range(len(lst)):
    print(lst[i], end=" ")