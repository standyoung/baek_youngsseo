# 'king':1, 'queen':1, 'bishop':2, 'rook':2, 'knight':2, 'pawn':8

chess_lst = [1, 1, 2, 2, 2, 8]
chess_inpt = list(map(int, input().split()))
chess_oupt = []

for i in range(len(chess_lst)):
    c = chess_lst[i] - chess_inpt[i]
    chess_oupt.append(c)
    # chess_oupt[i] = c 안됨 chess_oupt 리스트 사이즈가 정해지지 않았기 때문

print(*chess_oupt)