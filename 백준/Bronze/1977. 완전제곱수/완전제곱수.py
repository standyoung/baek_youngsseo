m = int(input())
n = int(input())

lst = []
num = 1

while True:
    square = pow(num, 2)
    if square >= m and square <= n:
        lst.append(square)
    num += 1

    if num > n:
        break

if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))
