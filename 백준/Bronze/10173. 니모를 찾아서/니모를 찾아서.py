import sys

while True:
    s = sys.stdin.readline().rstrip()

    if s == "EOI":
        break

    s = s.lower()
    s = s.split(" ")  # 리스트

    flag = False
    for i in range(len(s)):
        if "nemo" in s[i]:
            flag = True

    if flag == False:
        print("Missing")
    else:
        print("Found")
