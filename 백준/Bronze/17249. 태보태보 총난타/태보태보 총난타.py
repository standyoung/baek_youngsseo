import sys
jap = sys.stdin.readline().rstrip().replace("=", "")

left = 0
for i in range(len(jap)):
    if jap[i] == "(":
        break
    elif jap[i] == "@":
        left += 1

right = jap.count("@") - left

print(left, right)
