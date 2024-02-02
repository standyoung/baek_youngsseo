import sys

summ = 0

while True:
    n = int(sys.stdin.readline())

    if n == -1:
        print(summ)
        break

    summ += n
