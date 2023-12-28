sit = [0] * 101
n = int(input())

lst = list(map(int, input().split()))

for i in range(len(lst)):
    sit[lst[i]] = 1

check = 0
for i in range(len(sit)):
    if sit[i] == 1:
        check += 1

print(n - check)
