t = int(input())

for _ in range(t):
    n = int(input())

    n_1 = n+1

    if n_1 % int(str(n)[2:]) == 0:
        print("Good")
    else:
        print("Bye")
