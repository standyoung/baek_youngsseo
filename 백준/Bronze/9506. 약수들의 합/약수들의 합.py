import sys

while True:
    N = int(sys.stdin.readline())   # 초기화
    lst = []

    if N == -1: # while문 멈춤
        break
    else:
        for i in range(1,N):        # [주의점] 자기 자신 들어가면 안됨
            if (N%i) == 0:
                lst.append(i)       # 약수 리스트에 넣기

        if sum(lst) == N:
            print(N,"= ",end='')
            print(*lst, sep=" + ")  # *연산자 : 리스트 요소 하나씩 꺼내서 출력
        else:
            print("{} is NOT perfect.".format(N))