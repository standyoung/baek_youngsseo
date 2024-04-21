n = int(input())
lst = list(map(int, input().split()))
t = sum(lst) + (n-1)*8


day = t//24
time = t % 24
print(day, time)
