t = int(input())

for _ in range(t):
    m, k = map(str, input().split())
    m = int(m)

    if k == "C":
        lst = input().split()
        for i in range(m):
            lst[i] = ord(lst[i]) - 64
    elif k == "N":
        lst = list(map(int, input().split()))
        for i in range(m):
            lst[i] = chr(lst[i]+64)

    print(*lst, sep=" ")

# print(ord('A')) A = 65
