N, K = map(int, input().split())

lst = [i for i in range(1, N + 1)]
yo_lst = []

for _ in range(len(lst)):
    if len(lst) >= K:
        yo_lst.append(lst[K - 1])
        lst.remove(lst[K - 1])
        lst = lst[K - 1 :] + lst[: K - 1]
    else: # len(lst) < K
        K_ = K % len(lst)
        # 나머지 자리로 K 구함
        # K = 5 ; lst = [1,2,3] 이면 K % len(lst) = 2
        yo_lst.append(lst[K_ - 1])

        if lst[K_ - 1] != lst[-1]:
            lst.remove(lst[K_ - 1])
            lst = lst[K_ - 1 :] + lst[: K_ - 1]
        else: # 빼려는 수가 끝에 있다면 리스트 그냥 냅두기
            lst.remove(lst[K_ - 1])
    # print(yo_lst)
    # print(yo_lst[-1])
    # print()

print("<", end="")
print(*yo_lst, sep=", ", end="")
print(">", end="")

# yo = []
# lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# yo.append(lst1[10])
# lst1.remove(lst1[10])

# lst2 = lst1[10:] + lst1[:10]
# lst2.append(lst2[0])

# print(lst2)
# print(yo)
# [1,2,3,4,5]
# [3,4,5,1,2]
# print(9 % 8)
