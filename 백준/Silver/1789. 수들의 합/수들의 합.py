n = int(input())
summ = 0
number = 0

while True:
    number += 1 # 1+2+3+...+p > sum
    summ += number

    if summ > n:
        break

print(number-1)
