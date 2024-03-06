n = int(input())
ans = ""

while n >= 1:
    rem = n % 2
    n = n // 2
    ans = str(rem) + ans

ans = ans[::-1]

demical = 0
for i in range(len(ans)-1, -1, -1):
    demical += int(ans[len(ans)-1-i]) * pow(2, i)

print(demical)
