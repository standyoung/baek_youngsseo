import sys

T = int(sys.stdin.readline().rstrip())

# 일의 자리 수 = 데이터 처리 컴퓨터
# 1부터 10까지의 거듭제곱시 10으로 나누었을 때 일의 자리 패턴
lst = [
    [10],
    [1],
    [2, 4, 8, 6],
    [3, 9, 7, 1],
    [4, 6],
    [5],
    [6],
    [7, 9, 3, 1],
    [8, 4, 2, 6],
    [9, 1],
]

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    if a == 10:
        print(10)
    else:
        print(lst[a % 10][b % (len(lst[a % 10])) - 1])
# ans[a%10] -> 주어진 a의 뒷자리
# len(ans[a%10]) -> 주어진 a의 뒷자리가 정답으로 나올수있는 2차원 배열들이 담긴 배열의 길이 예) len([2,4,8,6])
