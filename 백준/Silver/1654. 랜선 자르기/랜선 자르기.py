import sys
k, n = map(int, input().split())


l = [int(sys.stdin.readline()) for _ in range(k)]

low = 1 # 랜선의 길이 구하기, 자연수
upper = max(l)

while low <= upper:
    cnt = 0 # 랜선 수를 카운팅하는 변수가 반복될때마다 초기화해야함
    mid = (low+upper)//2 # 중간값 설정

    for i in l:
        cnt += (i//mid) # 랜선을 자른 수
        # 802//200 = 4, 743//200 = 3, 457//200 = 2, 539//2 = 2

    if cnt >= n: # 랜선을 자른 수가 n보다 클 경우
        low = mid+1 # 랜선 늘리기
        mid = (low+upper)//2

    elif cnt < n: # 랜선을 자른 수가 n보다 작을 경우
        upper = mid-1 # 랜선 줄이기
        mid = (low+upper)//2

print(mid)
