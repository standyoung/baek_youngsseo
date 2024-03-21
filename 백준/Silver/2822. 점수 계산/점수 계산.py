import sys
lst = []
dic = {}

for i in range(8):
    n = int(sys.stdin.readline().rstrip())
    lst.append(n)
    dic[i+1] = n

sort_lst = sorted(lst)
top5 = sort_lst[-5:]  # [33, 48, 50, 64, 66]

print(sum(top5))

dic_k = list(dic.keys())

ans = []
for i in range(5):
    if top5[i] in lst:
        ans.append(lst.index(top5[i])+1)

ans.sort()
print(*ans, sep=" ")
