s = input()
s_list = [] # s 유니코드
ord_list = [] # A부터 Z까지 유니코드

for i in range(26):
    ord_list.append(i+97)

for i in range(len(s)):
    s_list.append((ord(s[i]))) # a:97, A:65
    # baekjoon [98, 97, 101, 107, 106, 111, 111, 110]
 
for i in range(len(ord_list)):
    if ord_list[i] in s_list :
        print(s_list.index(ord_list[i]),end=' ')
    else :
        print(-1, end=' ')