import sys

input = sys.stdin.readline()

N, M = map(int, input.split())

if M == 1 or M == 2:
    print("NEWBIE!")
elif M <= N and M != 1 and M != 2:
    print("OLDBIE!")
else:  # 뉴비도 올드비도 아니다
    print("TLE!")
