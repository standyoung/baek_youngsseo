n = int(input())

no_cute = 0
cute = 0

for _ in range(n):
    num = int(input())

    if num == 0:
        no_cute += 1
    elif num == 1:
        cute += 1

if cute > no_cute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
