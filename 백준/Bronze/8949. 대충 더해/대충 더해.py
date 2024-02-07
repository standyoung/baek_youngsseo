a, b = map(str, input().split())
num = 0
ans = ""

if len(a) == len(b):
    for i in range(len(a)):
        num = int(a[i])+int(b[i])
        ans += str(num)
else:
    if len(a) > len(b):
        dif = len(a)-len(b)  # 2
        ans = a[:dif]
        for i in range(len(b)):  # 0 1 2
            num = int(a[i+dif])+int(b[i])
            ans += str(num)

    elif len(b) > len(a):
        dif = len(b)-len(a)
        ans = b[:dif]
        for i in range(len(a)):
            num = int(b[i+dif])+int(a[i])
            ans += str(num)

print(ans)
