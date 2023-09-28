lst = []
for _ in range(5):
    score = int(input())
    if score >= 40:
        lst.append(score)
    else:
        lst.append(40)
print(sum(lst) // 5)