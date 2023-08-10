# 파일 이름의 길이는 모두 같다
# .은 상관없다
cnt = int(input())
fn_list = []
flag = [True]*51

for _ in range(cnt):
    file_name = input()
    fn_list.append(file_name)

# abcd
# abbd
# accd
for i in range(1,cnt):
    for j in range(len(fn_list[i])): # file_name 길이 고정
        if fn_list[i-1][j] != fn_list[i][j]: # 문자열 비교
            flag[j] = False

answer = ""
for i in range(len(fn_list[0])): # fn_list 요소 하나일 수도 있기 때문
    if flag[i] == True:
        answer += fn_list[0][i]
    else :
        answer += "?"
print(answer)