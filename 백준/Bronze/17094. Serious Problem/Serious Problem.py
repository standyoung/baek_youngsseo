import sys
n = int(input())
s = sys.stdin.readline().rstrip()

two = 0
e = 0
for i in range(n):
    if s[i] == '2':
        two += 1

    elif s[i] == 'e':
        e += 1

if two > e:
    print(2)
elif two < e:
    print('e')
else:
    print('yee')
