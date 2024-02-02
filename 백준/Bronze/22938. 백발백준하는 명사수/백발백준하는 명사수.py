import math
x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

d = math.sqrt((x1-x2)**2 + (y1-y2)**2)

if (max(r1, r2)-min(r1, r2) < d < r1+r2) or (max(r1, r2)-min(r1, r2) >= d) or d == 0:
    print("YES")

else:
    print("NO")