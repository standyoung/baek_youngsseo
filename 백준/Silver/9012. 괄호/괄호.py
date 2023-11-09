T = int(input())
flag = ""

for i in range(0, T):  # 6
    s = list(input())
    lst = []

    for j in range(0, len(s)):  # 7
        if s[j] == "(":
            lst.append("(")

        elif s[j] == ")":
            if len(lst) != 0 and lst[-1] == "(":
                lst.pop()

            elif len(lst) == 0:
                lst.append(")")

    if len(lst) != 0:
        flag = "NO"
    else:
        flag = "YES"

    print(flag)
