# 1259. 펠린드롬수

while True :
    p = input()
    if p == "0":
        break

    elif p != "0":
        if len(p) == 1 : # p:1,2,3,4,5...
            flag = "yes"
        else :
            if p[0] == "0": # ex) 무의미한 0 맨앞ㄴ
                flag = "no"
            else :
                s = len(p) // 2  # s는 중간 지점 인덱스
                for i in range(0,s+1,1): # 0~s
                    if p[i] != p[-(i+1)]: # 앞, 뒤 순서대로 비교
                        flag = "no"
                        break # for문 중단
                    else :
                        flag = "yes"
                    
    print(flag)

# print(1//2) --> 0
# print(2//2) --> 1
# print(3//2) --> 1