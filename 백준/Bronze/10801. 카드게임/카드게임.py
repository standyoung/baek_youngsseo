a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))
a, b = 0, 0

for i in range(10):
    if a_lst[i] > b_lst[i]:
        a += 1
    elif a_lst[i] < b_lst[i]:
        b += 1

if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('D')
