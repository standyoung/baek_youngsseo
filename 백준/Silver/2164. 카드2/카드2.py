from collections import deque

n = int(input())

if n == 1:
    print(1)
    exit(0)

lst = deque([i+1 for i in range(n)])

while True:
    lst.popleft()
    t1 = lst.popleft()
    lst.append(t1)

    if len(lst) == 1:
        print(lst[0])
        break
