a, b = map(int,input().split())

for i in range(1,max(a,b)+1):
    if a % i == 0 and b % i == 0:
        com_div = i
print(com_div)

a_, b_ = a, b
while (b>0):
    a, b = b, a % b

com_mp = (a_*b_) // a
print(com_mp)