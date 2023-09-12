import sys

T = int(sys.stdin.readline().rstrip())

# 일의 자리 수 = 데이터 처리 컴퓨터
# 1부터 10까지의 거듭제곱시 10으로 나누었을 때 일의 자리 패턴
lst = [
    [10],
    [1],
    [2, 4, 6, 8],
    [3, 9, 7, 1],
    [4, 6],
    [5],
    [6],
    [7, 9, 3, 1],
    [8, 4, 2, 6],
    [9, 1],
    [0],
]

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    a = a % 10

    if a in [1, 5, 6]:
        print(a)
    elif a in [4, 9]:
        b = b % 2
        if b == 0:  # 지수가 짝수
            print((a**2) % 10)
        else:
            print(a)
    elif a in [2, 3, 7, 8]:
        b = b % 4
        if b == 0:
            print((a**4) % 10)
        else:
            print((a**b) % 10)
    else:  # a == 0 : 10의 배수
        print(10)
