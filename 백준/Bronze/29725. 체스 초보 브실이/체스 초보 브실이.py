w = 0
b = 0
for _ in range(8):
    c = list(input())
    for i in range(8):
        if c[i] == '.':
            w += 0
            b += 0
        elif c[i] == 'K':
            w += 0
        elif c[i] == 'P':
            w += 1
        elif c[i] == 'N':
            w += 3
        elif c[i] == 'B':
            w += 3
        elif c[i] == 'R':
            w += 5
        elif c[i] == 'Q':
            w += 9
        elif c[i] == 'k':
            b += 0
        elif c[i] == 'p':
            b += 1
        elif c[i] == 'n':
            b += 3
        elif c[i] == 'b':
            b += 3
        elif c[i] == 'r':
            b += 5
        elif c[i] == 'q':
            b += 9
print(w-b)
