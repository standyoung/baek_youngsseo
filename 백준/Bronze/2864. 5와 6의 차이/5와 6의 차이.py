a, b = map(str, input().split())

a = a.replace('6', '5')
b = b.replace('6', '5')

minn = int(a) + int(b)

a = a.replace('5', '6')
b = b.replace('5', '6')

maxx = int(a) + int(b)

print(minn, maxx)
