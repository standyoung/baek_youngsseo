n = int(input())

a, b = map(int, input().split())
t = (a//2)+b

if t > n:
    print(n)
else:
    print(t)
