import sys
n = int(input())

cnt = 0

p = set()

for i in range(n): 
    s = sys.stdin.readline().rstrip()

    if s == "ENTER":
        cnt += len(p)
        p = set()
    else:
        p.add(s)

cnt += len(p)
print(cnt)