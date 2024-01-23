while True:
    s = input()

    if s == "#":
        break
    else:
        s = list(s)
        flag = 0  # 1의 개수
        for i in range(len(s)):
            if s[i] == "1":
                flag += 1

        if (flag % 2) == 0 or (flag == 0):  # 1이 짝수개이거나 0개일때
            if s[-1] == "e":
                s[-1] = "0"
            else:
                s[-1] = "1"
        else:
            if s[-1] == "e":
                s[-1] = "1"
            else:
                s[-1] = "0"

        print(''.join(s))
