N, K = map(int, input().split())

lst = [i for i in range(1, N + 1)]
yo_lst = []

for _ in range(len(lst)):
    if len(lst) >= K:
        yo_lst.append(lst[K - 1])
        lst.remove(lst[K - 1])
        lst = lst[K - 1 :] + lst[: K - 1]
    else:
        K_ = K % len(lst)
        yo_lst.append(lst[K_ - 1])
        if lst[K_ - 1] != lst[-1]:
            lst.remove(lst[K_ - 1])
            lst = lst[K_ - 1 :] + lst[: K_ - 1]
        else:
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
