t = int(input())

for _ in range(t):
    j, n = map(int, input().split())
    lst = []
    cnt = 0
    summ = 0

    for _ in range(n):
        r, c = map(int, input().split())
        lst.append(r*c)

    lst.sort(reverse=True)

    for n in lst:
        summ += n
        cnt += 1
        if summ >= j:
            print(cnt)
            break
