n = int(input())
cnt = 0
shom = "666"

number = 665

while True:
    number += 1

    if shom in str(number):
        cnt += 1

        if cnt == n:
            print(number)
            break
