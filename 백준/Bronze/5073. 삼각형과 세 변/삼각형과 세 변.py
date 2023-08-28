# 삼각형의 조건으로 크게 걸러줘야함
while True:
    lst = []
    a,b,c = map(int, input().split())
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.sort()  # 오름차순 정렬

    if a == b == c == 0:
        break
    elif a == b == c :
        print("Equilateral")
    elif lst[2] < lst[0]+lst[1]:    # 삼각형 조건 : 가장 긴변 < 나머지 두변의 합
        if a != b != c != a :
            print("Scalene")
        else:
            print("Isosceles")
    else:
        print("Invalid")
