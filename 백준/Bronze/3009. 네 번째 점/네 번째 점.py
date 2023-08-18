x_a, y_a = map(int,input().split())
x_b, y_b = map(int,input().split())
x_c, y_c = map(int,input().split())

# 조건문 지옥?..
if x_a == x_b:
    x_d = x_c
    if y_a == y_c:
        y_d = y_b
    elif y_b == y_c:
        y_d = y_a

elif x_b == x_c:
    x_d = x_a
    if y_b == y_a:
        y_d = y_c
    elif y_c == y_a:
        y_d = y_b

elif x_a == x_c:
    x_d = x_b
    if y_a == y_b:
        y_d = y_c
    elif y_c == y_b:
        y_d = y_a

print(x_d, y_d)