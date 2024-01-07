import sys
t = int(input())
for _ in range(t):
    n = int(input())
    note1 = list(map(int,sys.stdin.readline().rstrip().split()))

    dic1 = {}
    for i in note1:
        dic1[i] = 1

    m = int(input())
    note2 = list(map(int,sys.stdin.readline().rstrip().split()))

    for n in note2:
        if n in dic1.keys():
            print(1)
        else:
            print(0)
