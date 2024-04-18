p1, s1 = map(int, input().split())  # p홈경기
s2, p2 = map(int, input().split())  # s홈경기

p = p1+p2
s = s1+s2

if p > s:
    print("Persepolis")
elif p < s:
    print("Esteghlal")
elif p == s:
    p = p2
    s = s1
    if p > s:
        print("Persepolis")
    elif p < s:
        print("Esteghlal")
    else:
        print("Penalty")