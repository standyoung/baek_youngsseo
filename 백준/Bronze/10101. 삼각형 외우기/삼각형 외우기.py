angle_lst = []
for _ in range(3):
    angle = int(input())
    angle_lst.append(angle)

if sum(angle_lst) == 180 :
    if angle_lst[0] == angle_lst[1] == angle_lst[2] == 60:
        print("Equilateral")
    elif angle_lst[0] == angle_lst[1] or angle_lst[0] == angle_lst[2] or angle_lst[1] == angle_lst[2]:
        print("Isosceles")
    else:
        print("Scalene")
else :
    print("Error")