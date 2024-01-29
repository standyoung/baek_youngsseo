# a=97 z=122
n = int(input())

for _ in range(n):
    alpha = [0]*26
    s = input()
    s = s.lower()

    for i in range(len(s)):
        ix = ord(s[i])-97
        if ix >= 0 and ix <= 25:
            alpha[ix] += 1

    if 0 in alpha:
        ans = []
        for j in range(len(alpha)):
            if alpha[j] == 0:
                ans.append(chr(j+97))

        ans.sort()
        print('missing', end=" ")
        print(*ans, sep='')
    else:
        print('pangram')
