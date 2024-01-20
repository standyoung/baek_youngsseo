dic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
       7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
while True:
    day, month, year = map(int, input().split())
    if day == 0 and month == 0 and year == 0:
        break

    cnt = day

    if year % 4 == 0:
        if (year % 100 != 0) or (year % 400 == 0):
            dic[2] = 29

    for i in range(1, month):
        cnt += dic[i]

    print(cnt)

    dic[2] = 28
