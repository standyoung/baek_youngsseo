# 최소 공배수 = 두 수의 곱 / 최대 공약수

T = int(input())

for _ in range(T):
    fac_lst = []    # 공약수 리스트
    A,B = map(int, input().split())

    if A >= B: 
        for i in range(1,A):
            if (A % i) == 0 and (B % i) == 0:
                fac_lst.append(i)
    else :
        for i in range(1,B):
            if (A % i) == 0 and (B % i) == 0:
                fac_lst.append(i)

    if A == B:  # 같은 수가 들어올 때
        print(A)
    else:
        max_fac = max(fac_lst)
        print(int((A*B) / max_fac))