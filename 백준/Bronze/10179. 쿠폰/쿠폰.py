n = int(input())

for _ in range(n):
    price = float(input())
    price *= 0.8
    print("${:.2f}".format(price))
