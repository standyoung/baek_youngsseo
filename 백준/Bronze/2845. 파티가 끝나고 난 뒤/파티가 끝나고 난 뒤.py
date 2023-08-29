L, P = map(int, input().split())
news_lst = list(map(int, input().split()))

for i in range(5):
    print(news_lst[i]-(L*P),end=' ')