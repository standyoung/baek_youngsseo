for num in range(1000, 10000):
    two = 0
    six = 0
    ten = 0

    n = num
    while True:
        if n == 0:
            break
        two += n % 12
        n //= 12

    n = num
    while n != 0:
        if n == 0:
            break
        six += n % 16
        n //= 16

    n = num
    while n != 0:
        if n == 0:
            break
        ten += n % 10
        n //= 10

    if two == six == ten:
        print(num)
