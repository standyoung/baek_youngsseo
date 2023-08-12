A = int(input())
B = int(input())
C = int(input())
multiple = A*B*C # 17037300
multiple = str(multiple) # 문자열로 변환

count_dict = {}
num_list = ['0','1','2','3','4','5','6','7','8','9']

for i in range(len(num_list)):
    count = 0
    for j in range(len(multiple)): # 0 == 1,7,0..
        if num_list[i] == multiple[j] :
            count += 1
        count_dict[num_list[i]] = count  # {'0': 3, '1': 1, '2': 0, ...}

for i in range(len(num_list)):
    print(count_dict.get(num_list[i])) # input : dict.get(keys) -> ouput : value값