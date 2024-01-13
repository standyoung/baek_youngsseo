n = int(input())

home = 1  # 초기 숫자 1의 벌집 개수 1개
cnt = 1

for i in range(n):
    home += i*6  # 6의 배수로 누적해서 늘어남
    if n <= home:
        print(i+1)
        break