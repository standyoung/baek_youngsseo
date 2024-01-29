n = int(input())

lst = []

for _ in range(n):
    c = input()

    cnt = 0
    cnt += c.count("for")
    cnt += c.count("while")
    lst.append(cnt)

print(max(lst))
