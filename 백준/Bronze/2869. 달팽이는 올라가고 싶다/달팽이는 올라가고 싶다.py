a, b, v = map(int, input().split())
haru = a-b

if (v-b) % haru != 0:
    print((v-b)//(haru)+1)
else:
    print((v-b)//haru)

    # a + x(a-b) >= v
    # 올라가는거 + x(하루)
    # a-b + x(a-b) >= v-b
