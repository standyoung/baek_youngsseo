N = int(input())
score_lst = []

for _ in range(N):
    d1, d2, d3 = map(int,input().split())
    if d1 == d2 == d3:
        score_lst.append(10000+(d1*1000))
    elif d1 != d2 != d3 != d1:
        score_lst.append(max(d1,d2,d3)*100)
    else:
        lst = [d1,d2,d3]
        lst.sort()
        if lst[0] == lst[1] or lst[1] == lst[2]:
            score_lst.append(1000+(lst[1]*100))

print(max(score_lst))