x0, n = map(int, input().split())

for t in range(n):
    if x0 % 2 == 0:
        x0 = (x0//2) ^ 6

    else:
        x0 = (2*x0) ^ 6

print(x0)