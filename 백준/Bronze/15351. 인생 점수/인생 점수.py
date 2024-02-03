n = int(input())

for _ in range(n):
    s = input()
    s = s.replace(" ", "")
    score = 0

    for i in range(len(s)):
        score += ord(s[i]) - 64

    if score == 100:
        print("PERFECT LIFE")
    else:
        print(score)
