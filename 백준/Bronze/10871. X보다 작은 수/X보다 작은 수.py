lst = []
N, X = map(int, input().split()) # 10, 5
A = list(map(int, input().split())) # 수열

for i in range(len(A)):
    if A[i] < X :
        lst.append(A[i])

for i in range(len(lst)):
    print(lst[i],end=" ")