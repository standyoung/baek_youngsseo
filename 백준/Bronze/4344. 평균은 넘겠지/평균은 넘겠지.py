C = int(input())

for _ in range(C):
    score_lst = list(map(int, input().split()))
    N = score_lst[0]
    score_lst = score_lst[1:]

    cnt = 0
    mean = sum(score_lst)/N
    for i in range(N):
        if score_lst[i] > mean:
            cnt += 1
    ratio = (cnt / N)*100
    print("{:.3f}%".format(ratio))