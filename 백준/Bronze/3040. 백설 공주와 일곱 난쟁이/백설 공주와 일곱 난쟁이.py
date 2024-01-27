lst = []
for _ in range(9):
    lst.append(int(input()))

for i in range(9):
    for j in range(9):
        dwarf = sum(lst) - lst[i] - lst[j]

        if dwarf == 100:
            no_dwarf1 = lst[i]
            no_dwarf2 = lst[j]
            break

for i in range(9):
    if lst[i] != no_dwarf1 and lst[i] != no_dwarf2:
        print(lst[i])
