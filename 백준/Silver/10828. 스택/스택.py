import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    s = sys.stdin.readline().strip()

    if "pop" in s:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop(-1)
            
    elif "size" in s:
        print(len(stack))
        
    elif "empty" in s:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
    elif "top" in s:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            
    elif "push" in s:
        stack.append(int(s[5:]))
