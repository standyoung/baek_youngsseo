import sys
m = int(input())
S = set()

for _ in range(m):
    inpt = sys.stdin.readline().rstrip().split()
    if len(inpt) > 1:
        s, x = inpt[0], inpt[1]
        x = int(x)
    else:
        s = inpt[0]

    if s == "add":
        S.add(x)
    elif s == "remove":
        S.discard(x) # 없으면 넘어감 remove()는 오류
    elif s == "check":
        if x in S:
            print(1)
        else:
            print(0)
    elif s == "toggle":
        if x in S:
            S.discard(x)
        else:
            S.add(x)
    elif s == "all":
        S = set([i for i in range(1, 21)])
    elif s == "empty":
        S.clear()
