dic = {}

for _ in range(10):
    n = int(input())

    if n in dic.keys():
        dic[n] += 1
    else:
        dic[n] = 1

summ = 0
cnt = 0
for k, v in dic.items():
    summ += k*v
    cnt += v
print(summ//cnt)

max_v = max(list(dic.values()))

for k, v in dic.items():
    if v == max_v:
        print(k)
        break
