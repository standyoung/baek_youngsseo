n = int(input())
n_ = n
while True:
    if n == 1:
        print(f"1 bottle of beer on the wall, 1 bottle of beer.")
        print(f"Take one down and pass it around, no more bottles of beer on the wall.")
    elif n == 2:
        print(f"2 bottles of beer on the wall, 2 bottles of beer.")
        print(f"Take one down and pass it around, 1 bottle of beer on the wall.")
    elif n_ != 1 and n == 0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print(f"Go to the store and buy some more, {n_} bottles of beer on the wall.")
        break
    elif n_ == 1 and n == 0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print(f"Go to the store and buy some more, {n_} bottle of beer on the wall.")
        break
    else:
        print(f"{n} bottles of beer on the wall, {n} bottles of beer.")
        print(f"Take one down and pass it around, {n-1} bottles of beer on the wall.")
    n -= 1
    print()
