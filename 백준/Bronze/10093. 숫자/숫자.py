import sys

a, b = map(int, sys.stdin.readline().split())
num1 = min(a, b)
num2 = max(a, b)
n = num1 + 1
cnt = num2 - num1 - 1

if num1 == num2 or num2 == num1 + 1:
    cnt = 0
    print(cnt)

    exit(0)
print(cnt)
while n != num2:
    if n != b - 1:
        print(n, end=" ")
    if n == b - 1:
        print(n, end="")
    n += 1
