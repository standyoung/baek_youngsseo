n = input()
n_ = n

cnt = 0

while True:
    summ = 0
    for i in range(len(n)):
        summ += int(n[i])

    new = n[-1] + str(summ)[-1]
    n = new
    cnt += 1

    if int(n) == int(n_):
        print(cnt)
        break
