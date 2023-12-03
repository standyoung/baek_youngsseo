from collections import deque
import sys

n = int(sys.stdin.readline())

deq = deque()

for _ in range(n):
    c = sys.stdin.readline().rstrip()

    if "push_front" in c:
        c, num = c.split(" ")
        num = int(num)
        deq.appendleft(num)
        
    elif "push_back" in c:
        c, num = c.split(" ")
        num = int(num)
        deq.append(num)
        
    elif "pop_front" in c:
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[0])
            deq.popleft()
            
    elif "pop_back" in c:
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[-1])
            deq.pop()
            
    elif "size" in c:
        print(len(deq))
        
    elif "empty" in c:
        if len(deq) == 0:
            print("1")
        else:
            print("0")
            
    elif "front" in c:
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[0])

    elif "back" in c:
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[-1])
