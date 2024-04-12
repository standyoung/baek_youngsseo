n = int(input())
number = 1
cnt = 0

for i in range(1, n+1):
    number *= i

str_n = str(number)[::-1]
for j in str_n:
    if j == '0':
        cnt += 1
    elif j != '0':
        break
print(cnt)
