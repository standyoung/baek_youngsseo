import sys

num = int(sys.stdin.readline())  # 맨 끝이 개행문자까지 입력받음

# int(sys.stdin.readline()), sys.stdin.readline().split()
#  input = sys.stdin.readline

for _ in range(num):
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    print(a + b)