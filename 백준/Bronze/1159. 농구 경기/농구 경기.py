n = int(input())
surname = {}

for _ in range(n):
    s = input()
    if s[0] in surname:
        surname[s[0]] += 1
    else:
        surname[s[0]] = 1

s_lst = []
flag = False
for i in surname.keys():
    if surname[i] >= 5:
        s_lst.append(i)
        flag = True

if flag == False:
    print("PREDAJA")
else:
    s_lst.sort()
    print(*s_lst, sep="")
