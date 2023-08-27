# N의 약수들 중 K번째로 작은 수 출력
# 만일 약수의 개수 < K 이면 0 출력
lst = [] # lst : 약수 리스트
N, K = map(int, input().split())

for i in range(1,N+1):
    if (N % i) == 0:
        lst.append(i)

if len(lst) < K:
    print(0)
else :
    print(lst[K-1]) # K번째 약수