s = input()
k = input()

for i in range(len(s)):
    if s[i].isnumeric():
        s = s.replace(s[i], "#")

s = s.replace("#", "")

if k in s:
    print(1)
else:
    print(0)
