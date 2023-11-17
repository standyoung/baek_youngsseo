
T = int(input())

for i in range(T):
    N = int(input())
    lst = input().split()
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    print(min(lst), max(lst))
