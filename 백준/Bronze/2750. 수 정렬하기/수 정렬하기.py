n = int(input())
n_lst = []

for _ in range(n):
    input_num = int(input())
    n_lst.append(input_num)

n_lst = sorted(n_lst) # 오름차순

for i in range(len(n_lst)):
    print(n_lst[i])