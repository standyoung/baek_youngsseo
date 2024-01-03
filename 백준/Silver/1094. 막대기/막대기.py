x = int(input()) # x : 가지고 싶은 막대 길이
x_lst = [64]

flag = 0

if x == 64:
    print(1)
    exit(0)

# 64 / 2 => 32 32, 32 > 15 => 32
# 32 / 2 => 16 16, 16 > 15 => 16
# 16 / 2 => 8 8,  8 < 15 => 8,8
# 8 / 2 => 8 4 4, 12 < 15 => 8,4,4
# 4 / 2 => 8 4 2 2, 16 > 15 => 8,4,2
# 2 / 2 => 8 3 2 1 1, 15 = 15 => 8,4,2,1
i=0
while sum(x_lst) >= x:
    cut = (min(x_lst)//2) # 32

    if len(x_lst) > 1:
        x_lst[-1] = cut
        x_lst.append(cut)
    else :
        x_lst[0] = cut
        x_lst.append(cut)

    if sum(x_lst[:(len(x_lst)-1)]) >= x:
        x_lst.pop(-1)
    
    if sum(x_lst) == x:
        print(len(x_lst))
        break
    