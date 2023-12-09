t = int(input())
vowels_list = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
for _ in range(t):
    s = input()
    v_cnt = 0
    c_cnt = 0
    for i in range(len(s)):
        if s[i] in vowels_list:
            v_cnt += 1
        elif s[i] != " ":
            c_cnt += 1
    print(c_cnt, v_cnt)
