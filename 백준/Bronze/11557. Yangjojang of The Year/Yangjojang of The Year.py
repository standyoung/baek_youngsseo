T = int(input())
s_lst = []
l_lst = []

for _ in range(T): # 테스트 케이스 T개
    N = int(input())

    for i in range(N): # 학교 N개 
        s, l = map(str, input().split())
        l = int(l)
        s_lst.append(s)
        l_lst.append(l)
        max_l = l_lst.index(max(l_lst))
    print(s_lst[max_l])