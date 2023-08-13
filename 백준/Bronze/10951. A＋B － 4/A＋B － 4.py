# 입력이 끝날 때 읽어들이기
# except (예외처리)

while True :
    try : # 정상
        A, B = map(int, input().split())   
        if A == "" and B == "":
            break
        print(A+B)
    except: # 오류발생
        break