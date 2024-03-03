a, b, c, d = map(int, input().split())

lst = [a, b, c, d]
lst.sort()
print(abs((lst[0]+lst[3])-(lst[1]+lst[2])))
