n = int(input())
dict = {}
lst = []

for _ in range(n):
    name, dd, mm, yyyy = map(str, input().split())
    if len(mm) == 1:
        mm = "0" + mm
    if len(dd) == 1:
        dd = "0" + dd
    dict[yyyy + mm + dd] = name
    lst.append(yyyy + mm + dd)

lst.sort()

print(dict[lst[-1]])
print(dict[lst[0]])