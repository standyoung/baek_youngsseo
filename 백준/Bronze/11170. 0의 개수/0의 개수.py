t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    ans = 0

    for num in range(n, m+1):
        if "0" in str(num):
            ans += str(num).count("0")

    print(ans)
