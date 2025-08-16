from collections import deque

t = int(input())  # 몇번째로 인쇄되는지를 출력

for _ in range(t):
    n, idx = map(int, input().split())
    lst = list(map(int, input().split()))

    q = deque([[p, False] for p in lst])

    q[idx][1] = True
    cnt = 0
    # print(q)

    while True:
        cur = q.popleft()

        max_num = max(q)[0] if q else 0
        if cur[0] < max_num:
            q.append(cur)  # 높으면 뒤로 보냄
        else:
            cnt += 1
            if cur[1] == True:
                print(cnt)
                break
