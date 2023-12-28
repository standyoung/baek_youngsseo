import sys

n = int(sys.stdin.readline().rstrip())

small_lst = [0] * 1001
big = 0

for _ in range(n):
    d, c = map(str, sys.stdin.readline().rstrip().split())
    c = int(c)

    if c > 1000:
        big += 1

    if d == "jinju":
        charge = c

    elif c <= 1000 and d != "jinju":
        small_lst[c] += 1

small = 0
for i in range(charge + 1, len(small_lst)):
    small += small_lst[i]

print(charge)
print(small + big)
