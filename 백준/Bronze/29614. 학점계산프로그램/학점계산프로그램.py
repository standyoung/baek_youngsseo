S = input()

sum = 0
cnt = 0

for i in range(len(S)):
    if S[i] == "A":
        sum += 4.0
        cnt += 1
    elif S[i] == "B":
        sum += 3.0
        cnt += 1
    elif S[i] == "C":
        sum += 2.0
        cnt += 1
    elif S[i] == "D":
        sum += 1.0
        cnt += 1
    elif S[i] == "F":
        sum += 0.0
        cnt += 1
    elif S[i] == "+":
        sum += 0.5
print(sum / cnt)