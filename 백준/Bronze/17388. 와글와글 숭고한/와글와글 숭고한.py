s, k, h = map(int, input().split())

if (s+k+h) >= 100:
    print("OK")
else:
    m = min(s, k, h)
    if m == s:
        print("Soongsil")
    elif m == k:
        print("Korea")
    elif m == h:
        print("Hanyang")
