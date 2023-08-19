N = int(input())
ln_4 = "long int"
ln = "long "

N_share = N // 4

if N == 4:
    print(ln_4)
else:
    print((ln * (N_share - 1)) + ln_4)
