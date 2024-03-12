import sys
dic = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4,
       '>': 5, '&': 6, '%': 7, '/': -1}

while True:
    s = sys.stdin.readline().rstrip()

    if s == '#':
        break

    ans = 0
    for i in range(len(s)):
        ans += dic[s[i]]*pow(8, (len(s)-1-i))

    print(ans)
