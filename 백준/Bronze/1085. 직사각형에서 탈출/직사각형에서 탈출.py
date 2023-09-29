x, y, w, h = map(int, input().split())

mini_d = min(h - y, y, x, w - x)
print(mini_d)