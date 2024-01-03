import sys
while True:
    n, m = map(int, sys.stdin.readline().rstrip().split())

    if n==0 and m==0:
        break

    sang = [int(sys.stdin.readline().rstrip()) for _ in range(n)] # n
    sun = [int(sys.stdin.readline().rstrip()) for _ in range(m)] # m
    # 상근이와 선영이가 같은 CD를 여러장 가지고 있는 경우는 없음

    

    cnt = 0


    for i in range(n):
        search_value = sang[i] # 상근이의 cd번호

        start = 0
        end = m-1 # 선영이의 cd리스트 맨 끝

        while start <= end:

            mid = (start+end)//2
            mid_value = sun[mid] 

            if search_value == mid_value:
                cnt += 1
                break
            elif search_value < mid_value:
                end = mid - 1
            else:
                start = mid + 1

    print(cnt)