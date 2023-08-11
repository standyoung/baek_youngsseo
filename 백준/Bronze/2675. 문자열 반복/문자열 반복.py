num = int(input())
pos_list = [] # 인덱스
case_list = [] # 문자

for i in range(num):
    pos, case = input().split(" ")
    pos = int(pos)
    pos_list.append(pos)
    case_list.append(case)

for i in range(len(pos_list)): # 3,5
    for j in range(len(case_list[i])): # ABD, /HTP
        print(case_list[i][j]*pos_list[i],end='')
    print()