while True:
    fr_num, sc_num = map(int, input().split())
    if fr_num == 0 and sc_num == 0:
        break

    if fr_num < sc_num :
        if (sc_num % fr_num) == 0 :
            print("factor")
        else :
            print("neither") # 약수, 배수 둘 다 아님

    elif fr_num > sc_num :
        if (fr_num % sc_num) == 0 :
            print("multiple")
        else :
            print("neither") # 약수, 배수 둘 다 아님