import sys
from collections import deque

N = int(sys.stdin.readline())
N = deque([i for i in range(1, N + 1)])
A = deque(map(int, sys.stdin.readline().split()))
ans = deque()

while len(A):
    if A[-1] == 1:
        ans.appendleft(N.popleft())
        A.pop()

    elif A[-1] == 2:
        ans.appendleft(N.popleft())
        ans[0], ans[1] = ans[1], ans[0]
        A.pop()

    elif A[-1] == 3:
        ans.append(N.popleft())
        A.pop()

print(*ans)
