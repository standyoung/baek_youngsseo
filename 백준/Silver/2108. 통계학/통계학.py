import sys
t = int(sys.stdin.readline().rstrip())
lst = []
fre = {}

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    lst.append(n)

lst.sort()
for i in range(len(lst)):
    if lst[i] in fre.keys():
        fre[lst[i]] += 1
    else:
        fre[lst[i]] = 1

# print(lst)  # [-3, -2, -2, -1, -1]
# print(fre)  # {-3: 1, -2: 2, -1: 2}
val_lst = list(fre.values())
val_lst.sort()  # [1, 2, 2]

fre_ans = max(val_lst)

key_lst = list(fre.keys())
key_lst.sort()  # [-2, 1, 2, 3, 8]
# print(key_lst)  # [-3, -2, -1]


cnt = 0
for i in key_lst:
    if fre[i] == fre_ans:
        fre_2_val = i
        # print("fre_2_val :", fre_2_val)
        cnt += 1

    if cnt == 2:
        break

    if len(lst) == 1:
        fre_2_val = i
        break

print(int(round(sum(lst)/len(lst), 0)))
print(lst[len(lst)//2])
print(fre_2_val)
print(max(lst)-min(lst))