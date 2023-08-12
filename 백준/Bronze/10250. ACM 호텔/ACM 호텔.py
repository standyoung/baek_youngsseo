input_num = int(input())
test_data = []

for _ in range(input_num):
    H,W,N = map(int, input().split())
    hwn = [H,W,N]
    test_data.append(hwn) # [[6, 12, 10], [30, 50, 72]]

hotel = []
for k in range(len(test_data)):
    H = test_data[k][0]
    W = test_data[k][1]
    N = test_data[k][2]

    for i in range(1,W+1): # (1,13)
        for j in range(1,H+1): # (1,7)
            hotel.append(j*100 + i)
            
    print(hotel[N-1]) # N = 10이면 hotel[9]
    hotel = [] # 초기화