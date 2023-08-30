T = int(input())

for _ in range(T):
    lst = list(input().split())
    n = float(lst[0])
    for i in range(1,len(lst)):
        if lst[i] == '@':
            n *= 3
        elif lst[i] == '%':
            n += 5
        else:
            n -= 7
    print("{:.2f}".format(n))