import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split())

if b >= c:
    print(-1)
else:
    print(int(a / (c - b)) + 1)
    # 수입과 비용 같아지는 시점 : A + B*n = C*n
    # A = n(C-B)
    # A/(C-B) = n부터 수입과 비용같아져서
    # (A/(C-B))+1부터 순수익 발생함
    # !코드참고!
