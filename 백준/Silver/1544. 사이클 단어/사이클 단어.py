n = int(input())
lst = [input() for i in range(n)]  # 글자들 저장
dic = {}
ans = 0

for i in range(n):
    s = lst[i]  # picture

    if s not in dic:
        ans += 1

    for j in range(len(s)):  # 0 1 2 3..
        ss = s[1:]+s[0]  # turepic

        dic[s] = 1

        s = ss

print(ans)