s = input()
m = "MOBIS"

flag = "YES"

for i in range(len(m)):
    if m[i] not in s:
        flag = "NO"

print(flag)
