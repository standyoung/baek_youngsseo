N = int(input())
lst = []

for i in range(N+1):
    flag = int(i)       # N
    for j in str(i):
        flag += int(j)  # N의 각 자리수의 합

    if flag == N:
        print(i)
        exit(0)         # 프로그램 종료 <-> break
print(0)