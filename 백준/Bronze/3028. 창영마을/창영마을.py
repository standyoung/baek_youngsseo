def switch(alpha, lst):
    if alpha == 'A':
        lst[0], lst[1] = lst[1], lst[0]

    elif alpha == 'B':
        lst[1], lst[2] = lst[2], lst[1]

    elif alpha == 'C':
        lst[0], lst[2] = lst[2], lst[0]

    return lst


if __name__ == "__main__":
    s = input()
    lst = [1, 0, 0]

    for i in range(len(s)):
        switch(s[i], lst)

    for i in range(len(lst)):
        if lst[i] == 1:
            print(i+1)
