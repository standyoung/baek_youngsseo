lst = [int(input()) for i in range(6)]
print(sum(sorted(lst[:4], reverse=True)[0:3])+sorted(lst[4:], reverse=True)[0])
