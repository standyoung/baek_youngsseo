N = 5
lst = [list(input()) for _ in range(N)] # list(input()) : 문자열 한 글자씩 분리하여 리스트에 저장
# [['A', 'B', 'C', 'D', 'E'], ['a', 'b', 'c', 'd', 'e'], ['0', '1', '2', '3', '4'], ['F', 'G', 'H', 'I', 'J'], ['f', 'g', 'h', 'i', 'j']]

for i in range(15): # 한 행으로 된 입력의 길이 0~14 / 최대 15
    for j in range(5): # ?행 리스트의 길이
        if len(lst[j]) - 1 < i :
            continue
        else:
            print(lst[j][i],end='') 