import sys
n = sys.stdin.readline().rstrip()  # 6
left, right = 0, 0

for i in range(len(n)//2):  # 0 1 2
    left += int(n[i])

for i in range(len(n)//2, len(n)):
    right += int(n[i])

if left == right:
    print("LUCKY")
else:
    print("READY")