x, y = map(float, input().split())
seven = x / y # y그램당 x원 => 1그램당 x/y원

n = int(input())

min_bap = seven
for _ in range(n):
    xi, yi = map(float, input().split())
    other = xi / yi

    if other < min_bap:
        min_bap = other

print(min_bap * 1000)
