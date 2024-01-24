import sys
n = int(input())
dic = {}

for _ in range(n):
    name, score = sys.stdin.readline().rstrip().split()
    score = int(score)

    if score not in dic:
        dic[score] = [name]

    else:
        dic[score].append(name)

max_sc = max(dic.keys())

if len(dic[max_sc]) > 1:
    dic[max_sc].sort()
    print(dic[max_sc][0])
else:
    print(''.join(dic[max_sc]))
