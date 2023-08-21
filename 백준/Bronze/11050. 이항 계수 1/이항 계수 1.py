N, K = map(int, input().split()) # nCk : 이항계수 n!/(n-k)!k!
n = 1
k = 1
n_k = 1

for i in range(1, N + 1):
    n *= i
for j in range(1, K + 1):
    k *= j
for l in range(1, N - K + 1):
    n_k *= l

print(int(n / (k * n_k)))