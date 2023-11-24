N = int(input())

lst = [0] * 91

lst[0] = 0
lst[1] = 1
# lst[2] = 1
# lst[3] = 2
# lst[4] = 3

for i in range(2, N + 1):
    lst[i] = lst[i - 1] + lst[i - 2]

print(lst[N])
