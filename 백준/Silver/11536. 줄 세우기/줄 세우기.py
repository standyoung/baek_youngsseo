n = int(input())
lst = []

for i in range(n):
    s = input()
    lst.append(s)

sort_lst = sorted(lst)

if sort_lst == lst:
    if len(set(sort_lst) & set(lst)) == 1:
        print("NEITHER")
    else:
        print("INCREASING")
elif sort_lst[::-1] == lst:
    print("DECREASING")
else:
    print("NEITHER")
