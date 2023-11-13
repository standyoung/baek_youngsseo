import sys

cnt = []

for i in range(5):
    s = sys.stdin.readline()

    if "FBI" in s:
        cnt.append(i + 1)

if len(cnt) == 0:
    print("HE GOT AWAY!")
else:
    print(*cnt, sep=" ")
