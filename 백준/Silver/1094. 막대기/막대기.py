# 다른 참고 풀이 : https://sodehdt-ldkt.tistory.com/216
x = int(input()) # x : 가지고 싶은 막대 길이

stick = [64,32,16,8,4,2,1]

cnt = 0

for i in range(len(stick)):
    if x==0:
        break
    if stick[i] <= x:
        x -= stick[i]
        cnt += 1

print(cnt)