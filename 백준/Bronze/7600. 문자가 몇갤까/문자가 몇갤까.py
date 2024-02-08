while True:
    s = input().lower().replace(" ", "")

    if s == "#":
        break

    dic = {}
    for i in range(len(s)):
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            dic[s[i]] = 1

    print(len(dic.keys()))
