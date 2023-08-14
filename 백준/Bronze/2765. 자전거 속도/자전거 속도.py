# input: 바퀴의 지름(inch), 회전수, 걸린 시간(초)
# ouput: 총 이동거리(miles), 평균속도(miles/hour)
input_lst = []

while True:
    # 지름(inch), 회전수, 걸린시간
    d, num_rv, rq_time = input().split()
    d = float(d)
    num_rv = int(num_rv)
    rq_time = float(rq_time)
    
    if num_rv == 0 : # 종료조건
        break
    else :
        input_lst.append([d, num_rv, rq_time])

for i in range(len(input_lst)):
    d = input_lst[i][0]
    num_rv = input_lst[i][1]
    rq_time = input_lst[i][2]

    d_mile = 1/5280*1/12*d
    distance = 3.1415927*(d_mile)*num_rv # 이동거리 miles
    MPH =  distance / (rq_time / 3600.0)
    # 연산자 순서 고려!!
    # 실수라서 3600.0으로 나눔!! # 평균 속도의 단위 miles/hour

    print("Trip #{}: {:.2f} {:.2f}".format(i+1,distance,MPH))
    
    # 1마일은 5280피트
    # 1피트는 12인치
    # 1마일은 5280*12인치

    # 걸린시간 : 초
    # 속도는 : hour