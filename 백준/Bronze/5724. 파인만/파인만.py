while True:
    N = int(input())

    if N == 0:
        break
    sum = 0
    for i in range(1, N + 1):
        sum += (N - i + 1) ** 2
    print(sum)
