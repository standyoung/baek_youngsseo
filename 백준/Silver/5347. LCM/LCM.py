T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    a_ = a
    b_ = b

    while b != 0:
        c = a % b
        a = b
        b = c
    print(int(a_ * b_ / a))
