import sys

lst_09 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
dict_AF = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
ten = 0
S = sys.stdin.readline().rstrip()  # 문자

if len(S) == 1:
    if S[0] in dict_AF.keys():
        ten = dict_AF[S[0]]
    else:
        ten = S[0]
else:
    S = S[::-1]  # E3D -> D3E
    for i in range(len(S)):
        if S[i] in dict_AF.keys():
            ten += dict_AF[S[i]] * (16**i)
        else:
            ten += int(S[i]) * (16**i)

print(ten)
