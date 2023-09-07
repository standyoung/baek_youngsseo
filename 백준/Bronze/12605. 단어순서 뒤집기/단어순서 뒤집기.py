N = int(input())
i = 0
for _ in range(N):
    s = list(map(str, input().split()))
    i += 1
    print("Case #{}: ".format(i), end="")
    print(*s[::-1], sep=" ")