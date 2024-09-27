n = int(input())
lst = list(map(int, input().split()))
# print(lst)

lst.sort(reverse=True)

for i in range(n):
    lst[i] += i

# print(lst)

ans = max(lst) + 2
print(ans)
