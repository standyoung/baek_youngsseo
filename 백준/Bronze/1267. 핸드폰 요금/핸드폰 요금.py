n = int(input())
call = list(map(int, input().split()))

m = 0
y  = 0

for i in range(n):
    # 30초마다 10원
    y += (call[i]//30)*10 + 10


for i in range(n):
    # 60초마다 15원
    m += (call[i]//60)*15 + 15

# 싼 요금제 출력
if y<m:
    print("Y", y)
elif y>m:
    print("M", m)
else:
    print("Y M", y)