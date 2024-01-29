a, b, c = map(int, input().split())

lst = [0]*101
for _ in range(3):
    at, dt = map(int, input().split())
    for i in range(at, dt):  # a부터 d-1까지 1 2 3 3 2 1 1
        lst[i] += 1

asum = lst.count(1)*1*a
bsum = lst.count(2)*2*b
csum = lst.count(3)*3*c

print(asum+bsum+csum)
