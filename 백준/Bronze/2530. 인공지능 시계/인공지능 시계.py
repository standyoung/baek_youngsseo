a, b, c = map(int, input().split())
d = int(input())

c += d
c_ = c

if c >= 60:
    b += c_ // 60
    c = c_ % 60

if b >= 60:
    b_ = b
    a += b_ // 60
    b = b_ % 60

if a >= 24:
    a = a % 24

print(a, b, c)
