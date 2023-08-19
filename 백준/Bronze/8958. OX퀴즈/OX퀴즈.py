case_num = int(input())


for _ in range(case_num):  # 5
    flag = 0 # O이면 +1 / 초기화
    count = 0 # 점수 / 초기화
    a = input()

    for i in range(len(a)):
        if a[i] == "O":
            flag += 1 # O이면 flag + 1
            count += flag # flag와 count 더함

        elif a[i] == "X":
            flag = 0 # 0이면 flag = 0으로 초기화
            count += flag
    print(count)