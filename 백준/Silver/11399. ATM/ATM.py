n = int(input())
p = list(map(int, input().split()))
t = []
p.sort()

cnt = 0
for i in range(n):
    cnt += p[i]
    t.append(cnt)

print(sum(t))
