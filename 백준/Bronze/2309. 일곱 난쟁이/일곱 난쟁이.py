lst = []

for _ in range(9):
    height = int(input())
    lst.append(height)

lst.sort()
# [7, 8, 10, 13, 15, 19, 20, 23, 25]

lst_sum = sum(lst)

for i in range(9):
    for j in range(9):
        if lst_sum - (lst[i]+lst[j]) == 100:
            no_dwarf1 = lst[i]
            no_dwarf2 = lst[j]
            break

lst.remove(no_dwarf1)
lst.remove(no_dwarf2)
print(*lst, sep='\n')