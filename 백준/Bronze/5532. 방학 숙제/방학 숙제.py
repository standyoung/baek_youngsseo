import sys

L = int(sys.stdin.readline())
A = int(sys.stdin.readline()) # A(총)-C(하루) 국어
B = int(sys.stdin.readline()) # B(총)-D(하루) 수학
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

k_studying_day = A // C     # 국어 공부 최대
if A % C > 0:
    k_studying_day += 1     # 국어 공부 나머지 분량

m_studying_day = B // D     # 수학 공부 최대
if B % D > 0:
    m_studying_day += 1     # 수학 공부 나머지 분량

print(L-max(k_studying_day,m_studying_day)) # 노는날