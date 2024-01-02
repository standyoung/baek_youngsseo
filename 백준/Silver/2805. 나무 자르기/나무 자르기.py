import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
h = list(map(int, sys.stdin.readline().rstrip().split()))

max_h = max(h)
min_h = 0

while min_h<=max_h:
    cnt = 0
    mid = (max_h+min_h)//2

    # 나무의 높이가 최대한 높아야함
    # 절단기 높이는 최소 0부터 20까지
    for i in range(n):
        if h[i] >= mid:
            cnt += h[i] - mid
    
    # 적어도 m미터의 나무를 집에 가져가기 위해서
    if cnt >= m:
        min_h = mid + 1
    # 잘린나무가 작으면 절단기가 낮아져야함
    else:
        max_h = mid - 1

# 나무의 높이가 최대한 높아야하므로
print(max_h)
