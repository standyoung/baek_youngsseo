t = int(input())

for _ in range(t):

    n = int(input())
    lst = [0] * (n+1)  # 0번~n번

    for i in range(1, n+1):
        lst[i] = 1

    for i in range(2, n+1, 2):
        lst[i] = 0

    k = 3
    while True:
        if k == n+1:
            break

        for i in range(k, n+1, k):
            if lst[i] == 0:
                lst[i] = 1
            else:
                lst[i] = 0

        k += 1

    ans = 0
    for i in range(n+1):
        if lst[i] == 1:
            ans += 1
    print(ans)
