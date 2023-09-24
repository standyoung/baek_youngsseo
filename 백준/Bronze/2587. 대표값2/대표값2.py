num_lst = []
for _ in range(5):
    num = int(input())
    num_lst.append(num)

print(sum(num_lst) // 5)  # average

num_lst.sort()
print(num_lst[2])  # median