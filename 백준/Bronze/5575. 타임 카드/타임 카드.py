for _ in range(3):
    lst = list(map(int, input().split()))
    h = lst[3] - lst[0]
    m = lst[4] - lst[1]
    s = lst[5] - lst[2]

    if s < 0:
        s = s+60
        m = m - 1

    if m < 0:
        m = m+60
        h = h-1

    print(h, m, s)
