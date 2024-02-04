n = int(input())

if n == 1:
    print("*")
    exit(0)

for i in range(n):
    flag = 0
    while True:
        if flag == n:
            print()
            break

        print("*", end="")
        flag += 1

        if flag == n:
            print()
            break

        print(" ", end="")
        flag += 1

    flag = 0
    while True:
        if flag == n:
            print()
            break

        print(" ", end="")
        flag += 1

        if flag == n:
            print()
            break

        print("*", end="")
        flag += 1
