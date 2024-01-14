
s1, s2, s3 = map(int, input().split())

s1_lst = [i for i in range(1, s1+1)]  # [1,2,3]
s2_lst = [i for i in range(1, s2+1)]  # [1,2]
s3_lst = [i for i in range(1, s3+1)]  # [1,2,3]

lst = [0]*81

for i in s1_lst:
    for j in s2_lst:
        for k in s3_lst:
            lst[i+j+k] += 1

print(lst.index(max(lst)))
