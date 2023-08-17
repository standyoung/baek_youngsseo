pn_count = 0
n = int(input()) # 입력 : 소수의 개수
input_n = input() # 입력 : n개의 수

ip_n_lst = list(map(int, input_n.split())) # 입력된 n개의 수 리스트로
# ip_n_lst : [1,3,5,7]

for i in ip_n_lst: # i는 리스트 접근 제어변수 ex) 1,3,5,7
    count = 0 # count 초기화
    if i != 1: 
        for j in range(2,i+1): # i번째 요소 2부터 검사
            if i % j == 0 :
                count += 1 # count : 약수
        if count == 1: # count = 1이면 소수
            pn_count += 1

print(pn_count)