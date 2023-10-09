import math

M, N = map(int, input().split())

prime_lst = [True] * (N + 1)  # 모든 수가 소수임으로 가정

for i in range(2, int(math.sqrt(N)) + 1):  # n이 100이면 2부터 10까지, 2~10의 배수만 제거
    if prime_lst[i] == True:
        for j in range(i + i, N + 1, i):
            prime_lst[j] = False

prime_lst[1] = False

for i, v in enumerate(prime_lst[M : N + 1], start=M):
    if v == True:
        print(i)
