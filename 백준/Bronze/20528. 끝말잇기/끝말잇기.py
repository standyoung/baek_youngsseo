n = int(input())

lst = input().split()

flag = 1
for i in range(1, n):
    if lst[i][0] != lst[i-1][-1]:
        flag = 0
        break

print(flag)