t = int(input())
lst = []


while True:
    lst.append(t % 9)
    t = t // 9  # 11

    if t < 9:
        lst.append(t % 9)
        break

lst = lst[::-1]
if len(lst) == 2 and lst[0] == 0:
    lst.pop(0)
print(*lst, sep="")
