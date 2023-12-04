import sys

n = int(sys.stdin.readline())

n = "{:.300f}".format((1 / pow(2, n)))

idx = 0

for i in range(len(n) - 1, 1, -1):
    if n[i] != "0":
        idx = i
        break

print(n[: i + 1])
