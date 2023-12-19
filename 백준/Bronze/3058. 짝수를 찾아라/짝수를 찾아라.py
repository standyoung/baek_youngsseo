n = int(input())

for _ in range(n):
    lst = list(map(int, input().split()))
    even = []
    for i in range(7):
        if (lst[i] % 2) == 0:
            even.append(lst[i])
    print(sum(even), min(even))
