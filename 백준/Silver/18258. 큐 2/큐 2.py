# import queue

# que = queue.Queue()

# que.put('a')

# que.get()

# que.qsize()
# que.empty()
# que.full()

import sys
from collections import deque

## deque나 연결 리스트 활용하기
## pop하고 나서 나머지 인덱스를 앞으로 당기는데 O(n)의 시간이 걸림

N = int(sys.stdin.readline())
que = deque([])

for _ in range(N):
    com = sys.stdin.readline().split()

    if com[0] == "push":
        que.append(int(com[1]))
    elif com[0] == "pop":
        if len(que) == 0:  # empty면 True
            print(-1)
        else:
            print(que.popleft())  # 0번 빼기
    elif com[0] == "size":
        print(len(que))
    elif com[0] == "empty":
        if len(que) == 0:  # empty면 True
            print(1)
        else:
            print(0)
    elif com[0] == "front":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif com[0] == "back":
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
