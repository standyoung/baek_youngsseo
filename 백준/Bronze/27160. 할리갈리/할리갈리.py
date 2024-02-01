import sys
n = int(sys.stdin.readline().rstrip())
dic = {}

for _ in range(n):
    s, x = map(str, sys.stdin.readline().rstrip().split())
    x = int(x)

    if s in dic.keys():
        dic[s] += x
    else:
        dic[s] = x

if 5 in dic.values():
    print("YES")
else:
    print("NO")
