N, M = map(int, input().split())
x, y = [], []

lst = []
for _ in range(N):
    lst.append(list(map(int, input().split()))) 
    # list(map())
    # map()만 쓰면 메모리 주소값이 출력이 됨

# # 리스트 컨프리헨션
# lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
           x.append(i)
           y.append(j)
print(abs(x[0]-x[1])+abs(y[0]-y[1]))