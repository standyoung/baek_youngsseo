n = 0
while True:
    n = input()

    if n == "0":
        exit(0)

    while True:
        cnt = 0
        for i in range(len(n)):
            cnt += int(n[i])

        n = str(cnt)

        if len(n) == 1:
            print(cnt)
            break
