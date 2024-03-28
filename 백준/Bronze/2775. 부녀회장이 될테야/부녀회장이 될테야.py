t = int(input())
lst = []

for _ in range(t):
    k = int(input())
    n = int(input())
    cnt = 0

    floor = [m+1 for m in range(n)]  # 0층 1 2 3 4
    for i in range(1, k+1):
        new_floor = []
        for o in range(0, n):
            new_floor.append(sum(floor[:o+1]))
        floor = new_floor
    print(floor[n-1])

    # 0층부터 1호부터 있음
    # 0층의 i호에는 i명이 삼
