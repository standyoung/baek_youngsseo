num = int(input())
score = list(map(int, input().split()))
max_sc= max(score)

score_new = []

for i in range(num):
    score_new.append(score[i]/max_sc*100)
score_new_mean = sum(score_new)/num

print(score_new_mean)