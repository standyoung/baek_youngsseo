n = int(input())

ans = []  # 만점 맞은 학생

a = [((i-1) % 5)+1 for i in range(1, 11)]  # 학생들 답안

for j in range(1, n+1):
    s = list(map(int, input().split()))

    if a == s:
        print(j)
