n = int(input())
lst = []

for _ in range(n):
    lst.append(list(input()))

flag = True

for i in range(n):
    for j in range(n):
        if lst[i][j] != lst[j][i]:
            flag = False
            break

if flag == True:
    print("YES")
else:
    print("NO")
