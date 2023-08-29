C = int(input())

for _ in range(C):
    score_lst = list(map(int, input().split()))
    N = score_lst[0]
    score_lst = score_lst[1:]

    cnt = 0
    for i in range(N):
        if score_lst[i] > (sum(score_lst)/N):
            cnt += 1
    ratio = (cnt / N)*100
    print("{}%".format(ratio))
