a, b, c, d, e = map(int, input().split())

min_v = min(a, b, c, d, e)

while True:
    cnt = 0

    if min_v % a == 0:
        cnt += 1

    if min_v % b == 0:
        cnt += 1

    if min_v % c == 0:
        cnt += 1
        if cnt == 3:
            print(min_v)
            break

    if min_v % d == 0:
        cnt += 1
        if cnt == 3:
            print(min_v)
            break

    if min_v % e == 0:
        cnt += 1
        if cnt == 3:
            print(min_v)
            break

    min_v += 1
