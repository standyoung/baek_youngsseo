N, Y = map(str, input().split())
N = int(N)

cnt = 0
flag = 0
lst = []

for _ in range(N):
    lst.append(input())

if Y == "Y":
    print(len(set(lst)))

elif Y == "F":
    print(len(set(lst)) // 2)

else:
    print(len(set(lst)) // 3)
