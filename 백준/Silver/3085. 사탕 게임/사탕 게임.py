n = int(input())
lst = []
result = 0

for i in range(n):
    s = input()
    lst.append(list(s))


def cnt(lst):
    max_cnt = 1
    # 현재 시작점 사탕은 무조건 먹게되므로 1부터 시작
    for i in range(n):
        cnt = 1

        # 주어진 좌표로부터 좌 우 탐색
        for j in range(1, n):
            if lst[i][j] == lst[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

        # 주어진 좌표로부터 상 하 탐색
        cnt = 1
        for j in range(1, n):
            if lst[j][i] == lst[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
    return max_cnt


for i in range(n):
    for j in range(n):
        if j + 1 < n:
            # 좌, 우 변경
            temp = lst[i][j]
            lst[i][j] = lst[i][j + 1]
            lst[i][j + 1] = temp

            result = max(cnt(lst), result)
            result = max(cnt(lst), result)

            # 원상 복구
            temp = lst[i][j]
            lst[i][j] = lst[i][j + 1]
            lst[i][j + 1] = temp

        if i + 1 < n:
            # 상, 하 변경
            temp = lst[i][j]
            lst[i][j] = lst[i + 1][j]
            lst[i + 1][j] = temp

            result = max(cnt(lst), result)
            result = max(cnt(lst), result)

            # 원상 복구
            temp = lst[i][j]
            lst[i][j] = lst[i + 1][j]
            lst[i + 1][j] = temp

print(result)
