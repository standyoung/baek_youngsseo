n, m = map(int, input().split())
k = list(map(int, input().split()))

lst = [0]*(n+1)
for i in range(1, n+1):
    for j in range(m):
        if i % k[j] == 0:
            lst[i] = 1

sum = 0
for i in range(len(lst)):
    if lst[i] == 1:
        sum += i

print(sum)