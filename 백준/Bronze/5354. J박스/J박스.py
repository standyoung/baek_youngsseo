t = int(input())
for i in range(t):
    n = int(input())

    if n == 1:
        print("#")
    elif n == 2:
        print("##")
        print("##")
    else:
        print("#" * n)
        for _ in range(n - 2):
            print("#" + "J" * (n - 2) + "#")
        print("#" * n)

    if i != (t - 1):
        print()
