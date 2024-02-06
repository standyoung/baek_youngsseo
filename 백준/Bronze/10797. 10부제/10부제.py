n = input()
lst = list(map(str, input().split()))

cnt = 0
for i in range(5):
    if lst[i][-1] == n:
        cnt += 1

print(cnt)
