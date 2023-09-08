N = int(input())  # 4

print(" " * (N - 1) + "*")  # _ _ _ * 3 1

for i in range(N - 1):
    print(" " * (N - 2 - i) + "*" + " " * (2 * i + 1) + "*")

    #    2 * 1 *
    #  1 * 3 *
    # * 5 *