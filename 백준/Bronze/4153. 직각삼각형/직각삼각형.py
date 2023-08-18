while True: 
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break
    else: 
        lst = [a,b,c] # ex) 5,4,3
        lst = sorted(lst) # ex) 3,4,5

        if (lst[2])**2 == (lst[1])**2 + (lst[0])**2:
            print("right")
        else:
            print("wrong")