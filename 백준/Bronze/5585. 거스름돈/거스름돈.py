m = 1000-int(input())
ans = 0

ans += m//500
m = m % 500

ans += m//100
m = m % 100

ans += m//50
m = m % 50

ans += m//10
m = m % 10

ans += m//5
m = m % 5

ans += m//1

print(ans)
