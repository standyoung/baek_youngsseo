n = int(input())

while True:
    check = int(input())

    if check == 0:
        break

    if (check % n) == 0:
        print("{} is a multiple of {}.".format(check, n))
    else:
        print("{} is NOT a multiple of {}.".format(check, n))
