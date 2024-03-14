n = int(input())

s = input()
cnt = 0
bonus = 0

for i in range(n):
    if s[i] == 'O':
        cnt += (i+1) + bonus
        bonus += 1
    elif s[i] == 'X':
        bonus = 0

print(cnt)
