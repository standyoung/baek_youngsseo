n = int(input())

for i in range(n):
    lst = []
    a, b, c = map(int, input().split())

    lst = [a, b, c]
    lst.sort()

    print("Scenario #{}:".format(i + 1))
    if lst[2] ** 2 == (lst[0] ** 2) + (lst[1] ** 2):
        print("yes")
    else:
        print("no")

    if i != (n - 1):
        print("")
