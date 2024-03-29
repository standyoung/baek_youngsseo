import sys
m, n = map(int, input().split())
dic = {}

for _ in range(m):
    s, p = map(str, sys.stdin.readline().rstrip().split())
    dic[s] = p

for i in range(n):
    f_s = sys.stdin.readline().rstrip()
    print(dic[f_s])
