t = int(input())

for _ in range(t):
    n = int(input())
    summ = 0
    for i in range(1, n+1):
        if (i % 2) != 0:
            summ += i
    print(summ)
