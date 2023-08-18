# import sys
# a, b = map(int,sys.stdin.readline().split())

N = input()

for i in N:
    i = int(i)

N = sorted(N)
N = reversed(N)
N = list(N)

for i in range(len(N)):
    print(N[i],end='')   