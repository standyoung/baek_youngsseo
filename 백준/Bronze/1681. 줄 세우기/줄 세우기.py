n, l = map(str, input().split())
n = int(n)
lst = []

start = 1

while len(lst) != n:

    if l not in str(start):
        lst.append(start)

    start += 1

print(lst[n-1])
