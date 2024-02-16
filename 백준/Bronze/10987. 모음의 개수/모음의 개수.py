s = input()
m = ['a', 'e', 'i', 'o', 'u']

cnt = 0
for i in range(len(s)):
    if s[i] in m:
        cnt += 1
print(cnt)