N, M = map(int, input().split())
lst = []

for i in range(N):
    lst.append(i + 1)

for _ in range(M):
    i, j = map(int, input().split())
    lst[i - 1 : j] = lst[i - 1 : j][::-1]
    # lst[][::-1] -> lst[]의 역순 리스트 저장
    # lst[][::-1] != lst[::-1][]

print(*lst)
# *lst는 list 풀어서 end=' '로 출력