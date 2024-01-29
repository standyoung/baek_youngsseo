n = int(input())

for _ in range(n):
    p = int(input())

    p_lst = []
    for _ in range(p):
        c, name = map(str, input().split())
        c = int(c)
        p_lst.append([c, name])
    p_lst.sort()
    print(p_lst[-1][1])
