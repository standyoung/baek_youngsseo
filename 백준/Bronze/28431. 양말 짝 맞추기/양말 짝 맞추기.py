lst = [0]*10

for i in range(5):
    lst[int(input())] += 1

for i in range(len(lst)):
    if (lst[i] % 2) == 1:
        print(i)
        break
