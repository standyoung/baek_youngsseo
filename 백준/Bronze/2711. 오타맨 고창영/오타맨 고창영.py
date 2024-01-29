t = int(input())

for _ in range(t):
    n, s = map(str, input().split())
    n = int(n)
    s = s[:n-1] + s[n:]
    print(s)
