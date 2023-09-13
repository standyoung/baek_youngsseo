T = int(input())

for _ in range(T):
    n = int(input())
    lst = []
    i = 1
    j = 2
    sum = 0
    for i in range(1, n + 1):
        for j in range(2, n + 1):
            sum = i + j
            if (sum == n) and (i < j):
                lst.append([i, j])

    if len(lst) == 0:
        print("Pairs for {}:".format(n))
    else:
        print("Pairs for {}: ".format(n), end="")
        for i in range(len(lst)):
            if lst[i][0] == lst[-1][0]:
                print("{} {}".format(lst[i][0], lst[i][1]), end="")
            else:
                print("{} {}".format(lst[i][0], lst[i][1]), end=", ")
        print()