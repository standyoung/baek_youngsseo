n = int(input())

for _ in range(n):
    s1, s2 = map(str, input().split())
    s1 = list(s1)
    s2 = list(s2)

    s1.sort()
    s2.sort()

    flag = True
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                flag = False
                break
    else:
        flag = False

    if flag == True:
        print("Possible")
    else:
        print("Impossible")
