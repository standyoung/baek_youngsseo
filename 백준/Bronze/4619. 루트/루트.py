import sys
while True:
    b, n = map(int, input().split())

    if b == 0 and n == 0:
        exit(0)

    i = 0

    while i**n < b:
        i += 1

    if abs(i**n-b) < abs((i-1)**n-b):
        print(i)
    else:
        print(i-1)
