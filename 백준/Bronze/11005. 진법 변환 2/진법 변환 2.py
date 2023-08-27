import sys
input = sys.stdin.readline()
N, B = map(int, input.split())      # 60466175 # 36

r_lst = []
share = 1

num_lst = [i for i in range(10)]
str_lst = [i for i in range(65,91)] # A:65~Z:90

while True:
    if share == 0:
        break
    else:
        share = N // B
        rest = N % B
        r_lst.append(rest)          # 나머지
        N = share

r_lst = r_lst[::-1] # 순서 반대로

for i in range(len(r_lst)):
    if r_lst[i] in num_lst:
        print(r_lst[i], end='')
    elif r_lst[i] not in num_lst:
        r = r_lst[i]+55
        if r in str_lst:            # A가 10이니까
            print(chr(r), end='')