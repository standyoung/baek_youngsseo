# 시간 제한 2초 & 입력 1백만개 -> for문 2개 쓰나 생각해야함

# N의 분해합 = N + N의 각 자리수의 합
# M의 분해합 = N -> M이 N의 생성자
import sys
N = int(sys.stdin.readline())

for i in range(1,N+1):
    div_hap = i # 216
    for j in str(i):
        div_hap += int(j) # 2+1+6

    if div_hap == N:
        print(i)    # 198
        exit(0)     # 프로그램 종료 <-> break(반복문)
                    # 가장 작은 생성자가 구해지게 프로그램 종료
print(0)            # N이상 돌면 생성자가 없음