N = int(input())
one, two, three = 0,0,0

for i in range(1,N+1):
    one += i
    two += i
    three += i**3

two = two**2 # (1+2+3+4+5)^2
print(one, two, three, sep='\n')