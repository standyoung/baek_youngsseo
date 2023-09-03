# a:97 z:122
L = int(input())
S = list(input())
for i in range(len(S)):
    S[i] = ord(S[i]) - 96

H = 0
M = 1234567891
r = 31
for i in range(L):
    H += (S[i]*((r)**i)) % M

print(H)