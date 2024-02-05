n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    a_, b_ = a, b

    while b > 0:
        a, b = b, a % b
    print((a_*b_)//a, a)
