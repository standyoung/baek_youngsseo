A, B = map(int, input().split())
C = int(input())

B = B + C

A += (B//60) # 추가 시간
B %= 60 # 추가 분
A %= 24 # 24시간을 넘는다면
print(A, B)