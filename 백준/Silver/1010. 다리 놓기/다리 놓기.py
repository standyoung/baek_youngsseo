import math

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    case = math.factorial(m) // (math.factorial(m - n) * math.factorial(n))
    print(case)
