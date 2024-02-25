a = input()
b = input()
n = ""

for i in range(len(max(a, b))):
    n = n + a[i] + b[i]

cnt = 0

while True:
    summ = ""

    for i in range(len(n)):
        s = list(map(int, n[i:i+2]))  # int

        if len(s) == 2:
            p = sum(s)
            summ += str(p)[-1]

    n = summ

    if len(n) <= 2:
        print(n)
        break
