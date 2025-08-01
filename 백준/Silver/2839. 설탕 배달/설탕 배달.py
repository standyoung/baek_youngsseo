import sys
n = int(sys.stdin.readline().rstrip())
flag = False
ans = []

for i in range(0, n):
    for j in range(0, n):
        if ((3 * i) + (5 * j)) == n:
            ans.append(i+j)
            flag = True
            break

if flag == True:
    print(min(ans))
else:
    print(-1)