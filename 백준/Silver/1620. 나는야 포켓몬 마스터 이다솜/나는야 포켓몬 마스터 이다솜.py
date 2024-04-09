import sys
n, m = map(int, input().split())
poketmon = {sys.stdin.readline().rstrip(): (i+1) for i in range(n)}
poketmon_value = {v: k for k, v in poketmon.items()}
p = [sys.stdin.readline().rstrip()
     for _ in range(m)]

for i in range(m):
    if p[i] in poketmon.keys():
        print(poketmon[p[i]])
    else:
        print(poketmon_value[int(p[i])])
