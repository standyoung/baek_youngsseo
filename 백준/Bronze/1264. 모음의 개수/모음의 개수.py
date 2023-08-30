vowel_lst = ['a','e','i','o','u']
while True:
    s = input().replace(' ','')
    if s == "#":
        break
    else:
        s = s.lower()

        cnt = 0
        for i in range(len(s)):
            if s[i] in vowel_lst:
                cnt += 1
    print(cnt)