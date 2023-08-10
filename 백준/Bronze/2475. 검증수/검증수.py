n_sum = 0
n = list(map(int, input().split(" ")))

for i in range(5):
    n_sum += n[i]**2
    
val_num = n_sum % 10
print(val_num)