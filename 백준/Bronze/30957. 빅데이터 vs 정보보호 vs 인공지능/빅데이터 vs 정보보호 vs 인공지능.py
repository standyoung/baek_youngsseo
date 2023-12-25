# n = int(input())
# # 2 = 1 + 1
# # 3 = 2 + 2
# # 5 = 3 + 2
# # 8 = 5 + 3

# # 1 n = 1
# # 4 = 2(1 + 1) n = 2
# # 10 = 2(2 + 1 + 1 + 1) n = 3
# # 16 = 2(3 + 2 + 2 + 1) n = 4
# # 26 = 2(5 + 3 + 2 + 3) n = 5
# # 42 = 2(8 + 5 + 3 + 5) n = 6

n = int(input())
a_cnt, b_cnt, s_cnt = 0, 0, 0
s = input()

for i in range(len(s)):
    if s[i] == "S":
        s_cnt += 1
    elif s[i] == "B":
        b_cnt += 1
    else:
        a_cnt += 1

if s_cnt == b_cnt == a_cnt:
    print("SCU")
elif max(s_cnt, b_cnt, a_cnt) == a_cnt and max(s_cnt, b_cnt, a_cnt) == b_cnt:
    print("BA")
    exit(0)
elif max(s_cnt, b_cnt, a_cnt) == b_cnt and max(s_cnt, b_cnt, a_cnt) == s_cnt:
    print("BS")
    exit(0)
elif max(s_cnt, b_cnt, a_cnt) == s_cnt and max(s_cnt, b_cnt, a_cnt) == a_cnt:
    print("SA")
    exit(0)
elif max(s_cnt, b_cnt, a_cnt) == a_cnt:
    print("A")
elif max(s_cnt, b_cnt, a_cnt) == b_cnt:
    print("B")
elif max(s_cnt, b_cnt, a_cnt) == s_cnt:
    print("S")  ###
