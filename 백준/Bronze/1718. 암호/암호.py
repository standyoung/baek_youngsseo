s_ = input()
s_key = input()

s = []
for i in range(len(s_)):
    for j in range(len(s_[i])):
        s.append(s_[i][j])

p = []
for i in range(len(s)):
    if s[i] == " ":
        p.append(" ")
    else:
        if i >= len(s_key):
            j = i % len(s_key)
            ch = ord(s[i]) - (ord(s_key[j]) - 96)  # n - 12
            if ch < 97:
                ch = 123 - (ord("a") - (ord(s[i]) - (ord(s_key[j]) - 96)))
            p.append(chr(ch))

        else:
            ch = ord(s[i]) - (ord(s_key[i]) - 96)  # n - 12
            if ch < 97:
                ch = 123 - (ord("a") - (ord(s[i]) - (ord(s_key[i]) - 96)))
            p.append(chr(ch))
print(*p, sep="", end="")
