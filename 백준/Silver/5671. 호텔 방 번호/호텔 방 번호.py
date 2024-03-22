while True:
    try:
        n, m = map(int, input().split())
        cnt = 0

        for num in range(n, m+1):
            str_num = str(num)
            dic = {i: 0 for i in range(0, 10)}

            for j in range(len(str_num)):
                dic[int(str_num[j])] += 1

            if 2 not in dic.values() and 3 not in dic.values() and 4 not in dic.values():
                cnt += 1

        print(cnt)

    except EOFError:
        break
