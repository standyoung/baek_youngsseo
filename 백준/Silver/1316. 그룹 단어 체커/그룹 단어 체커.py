n = int(input())
count = 0

for _ in range(n):
    s_lst = input()
    flag = 0  # 문자 입력받을 때마다 초기화

    # 문자열 길이 1 or 1이상
    if len(s_lst) == 1:
        flag = 1
    else:
        for i in range(len(s_lst) - 1):  # ex) new range(2) -> 0,1
            if s_lst[i] != s_lst[i + 1]:  # 현재와 다음이 같지 않을 때
                if s_lst[i] in s_lst[i + 1 :]:  # 다음 이후 또 나올시에 flag = 0
                    flag = 0
                    break
                else:
                    flag = 1
            elif s_lst[i] == s_lst[i + 1]:  # 리스트 모든 요소 같다면 flag 1
                flag = 1
    count += flag
print(count)