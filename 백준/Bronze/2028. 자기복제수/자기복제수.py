t = int(input())

for _ in range(t):
    n = int(input())

    flag = n**2

    n = str(n)
    flag = str(flag)

    if flag[-len(n) :] == n:
        print("YES")
    else:
        print("NO")
