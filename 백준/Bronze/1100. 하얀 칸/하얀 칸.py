chesspan = [list(input()) for _ in range(8)]

ans = 0
for i in range(8):
    for j in range(8):
        if ((i+j) % 2 == 0) and (chesspan[i][j] == 'F'):
            ans += 1

print(ans)
