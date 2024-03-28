summ = 0
lst = [int(input()) for _ in range(10)]
sum_lst = []
dic = {}

for n in lst:
    summ += n
    sum_lst.append(summ)

for i in range(10):
    dic[abs(100-sum_lst[i])] = sum_lst[i]

min_k = min(list(dic.keys()))

print(dic[min_k])
