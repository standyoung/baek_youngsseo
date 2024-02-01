import sys
dic = {}
lst = []

while True:

    try:
        s = input()

        s = s.replace(" ", "")
        s = list(s)

        for i in range(len(s)):
            if s[i] in dic.keys():
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1

    except:
        break

ans = []
max_v = max(dic.values())

for k, v in dic.items():
    if v == max_v:
        ans.append(k)

ans.sort()

print(*ans, sep="")
