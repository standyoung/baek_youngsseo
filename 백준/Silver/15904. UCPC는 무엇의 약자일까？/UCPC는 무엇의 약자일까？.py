
s = input()
lst = []
ucpc = ['U', 'C', 'P', 'C']
idx = 0
flag = False

for i in range(len(s)):

    if ord(s[i]) >= 67 and ord(s[i]) <= 85:
        if s[i] == ucpc[idx]:
            idx += 1
            if idx == 4:
                break

if idx == 4:
    flag = True

if flag == True:
    print("I love UCPC")
else:
    print("I hate UCPC")

# print(ord("A"))
# ord("U") 85
# ord("C") 67
# ord("P") 80

# ord("A") 65
