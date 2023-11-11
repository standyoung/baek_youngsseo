import sys

N = int(sys.stdin.readline())
que = []

for i in range(N):
    s = sys.stdin.readline().strip()

    if "pop" in s:
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
            que.pop(0)
            
    elif "size" in s:
        print(len(que))
        
    elif "empty" in s:
        if len(que) == 0:
            print(1)
        else:
            print(0)
            
    elif "front" in s:
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
            
    elif "back" in s:
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
            
    elif "push" in s:
        que.append(int(s[5:]))
