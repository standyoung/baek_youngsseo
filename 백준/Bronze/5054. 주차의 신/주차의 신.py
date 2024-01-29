t = int(input())

for i in range(t):
    n = int(input())
    store = list(map(int, input().split()))
    store.sort()

    ans = 0
    for i in range(1, n):
        ans += store[i] - store[i-1]
    print(ans*2)
