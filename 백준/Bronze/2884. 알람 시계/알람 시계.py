H, M = map(int, input().split())
# import time을 한다면?.. 하지만 이렇게 하는건 아닐듯
# tm_hour	시	범위: 0~23
# tm_min	분	범위: 0~59

M_d = M - 45 # -15(분)

if M_d < 0 :
    H_d = H - 1
    M_d = M_d + 60
    if H_d < 0 :
        H_d = 23
        print(H_d,M_d)
    else :
        print(H_d,M_d)

else :
    print(H,M_d)