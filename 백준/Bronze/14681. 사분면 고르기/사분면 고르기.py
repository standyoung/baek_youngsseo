x = int(input())
y = int(input())

if x > 0 and y > 0:
    quadrant = 1
elif x > 0 and y < 0:
    quadrant = 4
elif x < 0 and y > 0:
    quadrant = 2
else :
    quadrant = 3

print(quadrant)