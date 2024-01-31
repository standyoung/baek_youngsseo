s = input()

if len(s) < 5:
    print("not cute")
else:
    if s[-5:] == "driip":
        print("cute")
    else:
        print("not cute")
