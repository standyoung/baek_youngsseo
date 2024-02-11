n, k = map(int, input().split())
lst = []

for i in range(1, k+1):
    lst.append(int(str(n*i)[::-1]))

print(max(lst))
