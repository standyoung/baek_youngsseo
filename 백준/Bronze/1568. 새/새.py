n = int(input())

# k = 1 1마리 날아감 n = 13
# k = 2 2마리 n = 13 - 2 = 11
# k = 3 11-3 8
# k= 4 8-4 4
# k=5 4
# k=1 4-1 3
# k=2 3-2 1
# k=1 1-1

k = 1
cnt = 0
while True:
    if n >= k:
        n = n - k
        k += 1
        cnt += 1

    else:
        k = 1

    if n == 0:
        break

print(cnt)
