N = int(input())
N_lst = list(map(int, input().split()))
v = int(input())

count = 0

for i in range(len(N_lst)):
    if v == N_lst[i]:
        count += 1
print(count)