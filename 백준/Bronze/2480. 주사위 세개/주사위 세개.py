same_eye = 0

d1, d2, d3 = map(int, input().split())

if d1 == d2 and d2 != d3:
    print(1000+d1*100)
elif d2 == d3 and d3 != d1:
    print(1000+d2*100)
elif d1 == d3 and d1 != d2:
    print(1000+d1*100)
elif d1 == d2 == d3:
    print(10000+d1*1000)
else:
    lst = [d1,d2,d3]
    max_d = max(lst)
    print(max_d*100)