import sys

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    com = sys.stdin.readline()

    if com[0] == "1":
        lst.append(int(com[2:]))
    elif com[0] == "2":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
            lst.pop()
    elif com[0] == "3":
        print(len(lst))
    elif com[0] == "4":
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    else:  ## '5'
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
