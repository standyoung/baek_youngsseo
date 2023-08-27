# 실수는 정수로 바꾸는게 좋음
T = int(input())

for _ in range(T):
    coin_lst = [25,10,5,1]
    C = int(input())

    for i in range(len(coin_lst)):
        change = C // coin_lst[i]   # 거스름돈
        print(change, end=' ')
        C %= coin_lst[i]            # 나머지는 다음 거스름돈으로 넘어감
    print()