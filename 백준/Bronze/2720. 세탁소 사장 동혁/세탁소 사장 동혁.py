# 0.03 // 0.01 = 2.0
# 0.03 / 0.01 = 3.0
# 실수를 정수로 바꿀 때 진짜 조심해야함
T = int(input())

for _ in range(T):
    change_lst = []
    C = int(input())
    C *= 0.01              # C의 단위 센트

    q = int(C / 0.25)
    change_lst.append(q)
    C = round(C - (0.25 * q),2)

    d = int(C / 0.10)
    change_lst.append(d)
    C = round(C - (0.10 * d),2)

    n = int(C / 0.05)
    change_lst.append(n)
    C = round(C - (0.05 * n),2)

    p = int(C / 0.01)
    change_lst.append(p)

    print(*change_lst)