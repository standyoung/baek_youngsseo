N = int(input())

for i in range(N):
    print((" " * (N-1-i))+("*" * (2*i+1)))

for j in range(N-1):
    print((" " * (j+1))+("*" * (2*(N-1)-(2*j+1))))