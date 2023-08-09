A, B, C = map(int, input().split(" "))
encounter = int(input()) # 참여한 동아리 수
lst = []
lst_club = []
# 종료조건.. encounter * 3인

for _ in range(encounter):
    hap = 0 # 엄청난 사실
    for _ in range(3) :
        a,b,c = map(int, input().split(" "))
        hap += a*A + b*B + c*C 
    lst.append(hap)

print(max(lst))