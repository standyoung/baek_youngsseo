n = input()
f = int(input())

for i in range(0, 10):
    for j in range(0, 10):
        n = n[:-2]+str(i)+str(j)
        num = int(n)

        if (num % f) == 0:
            print(str(i)+str(j))
            exit(0)