def hap(N):
    if len(str(N)) == 1:
        return N
    else:
        cnt = 0
        for i in str(N):
            cnt += int(i)
        N = cnt
        return hap(N)

while True:
    N = int(input())

    if N == 0:
        break
    else:
        result = hap(N)
        print(result)