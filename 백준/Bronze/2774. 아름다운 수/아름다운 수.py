t = int(input())

for _ in range(t):
    dic = {}
    x = input()

    for i in range(len(x)):
        dic[x[i]] = 1

    print(len(dic.keys()))
