n = int(input())
fac = 1

if n == 0 :
    print(1)

else :
    for i in range(2,n+1):
        fac *= i
    print(fac)