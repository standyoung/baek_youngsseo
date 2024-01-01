import sys

t = int(input())

for _ in range(t):
    a, b = map(int,input().split())
    a_lst = list(map(int,input().split()))
    b_lst = list(map(int,input().split()))
    a_lst.sort() # 1 1 3 7 8
    b_lst.sort() # 1 3 6

    st = 0
    cnt = 0
    for i in range(a): # 1 1 3 7 8 -> 5만큼
        while True:
            if st<=(b-1) and (a_lst[i] > b_lst[st]):
                st += 1
            else:
                cnt += st
                break
    
    print(cnt)