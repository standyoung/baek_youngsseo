from itertools import *
N, M = map(int, input().split())

card_lst = list(map(int, input().split()))
# [5, 6, 7, 8, 9]

hap_lst = list(map(sum,(combinations(card_lst,3))))
hap_lst = sorted(hap_lst) # 오름차순 정렬
# [18, 19, 20, 20, 21, 22, 21, 22, 23, 24]

flag = 0
for i in range(len(hap_lst)):
    if hap_lst[i] <= M :
        flag = max(flag, hap_lst[i])

    elif hap_lst[i] > M : # 탈출
        break

print(flag)