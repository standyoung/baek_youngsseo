
# A:65 Z:90
# a:97 z:122
# " ":32
# 0:48 9:57

while True:

    try:
        s = input()
        so, dae, num, space = 0, 0, 0, 0
        for i in range(len(s)):
            if ord(s[i]) >= 48 and ord(s[i]) <= 57:
                num += 1
            elif ord(s[i]) >= 65 and ord(s[i]) <= 90:
                dae += 1
            elif ord(s[i]) >= 97 and ord(s[i]) <= 122:
                so += 1
            elif ord(s[i]) == 32:
                space += 1

        print(so, dae, num, space)

    except EOFError:
        break
