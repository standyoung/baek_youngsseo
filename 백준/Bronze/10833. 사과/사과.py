n = int(input())
cnt = 0

for _ in range(n):
    stu, apple = map(int, input().split())
    cnt += apple % stu

print(cnt)
