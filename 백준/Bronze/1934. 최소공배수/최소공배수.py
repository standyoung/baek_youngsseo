import sys
T = int(sys.stdin.readline())

for _ in range(T):
    A,B = map(int, sys.stdin.readline().split())
    A_, B_ = A, B # 처음 A, B 저장

    while(B>0):
        A, B = B, A % B
        # A = 최대 공약수 -> 유클리드 호제법 이용
        # 최대 공배수 -> 두 수의 곱 // 최대 공약수
    
    print((A_*B_)//A)