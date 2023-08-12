count_dict = {}
s = input()
s_upper = s.upper() # 대문자로 변환

list_s = list(set(s_upper)) # 알파벳 집합 리스트로 변환

# s_upper : MISSISSIPI
# list_s : ['M', 'S', 'P', 'I']
for i in range(len(list_s)): # (0,4)
    count = 0
    for j in range(len(s_upper)): # (0,9)
        if list_s[i] == s_upper[j] : # M == M,I,S,S,I,P..
            count += 1
        count_dict[list_s[i]] = count

count_list = list(count_dict.values())
count_max = max(count_list)

flag = 0
for i in range(len(count_list)):
    if count_list[i] == count_max:
        flag += 1

count_dict_r = {v:k for k,v in count_dict.items()}

if flag >= 2 :
    print("?")
else :
    print(count_dict_r.get(count_max))