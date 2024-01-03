import sys

n = int(input())
wd = [[] for _ in range(20001)] # word dictionary

s = list(set(sys.stdin.readline().rstrip() for _ in range(n))) # 중복 단어 제거

for i in range(len(s)):
    wd[len(s[i])].append(s[i])

for j in range(20001):
    wd[j].sort()

for w in wd:
    if w != []:
        print(*w,sep="\n")