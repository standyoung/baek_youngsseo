N = int(input())        # 몇 번 덮어씌우실래요?
bef_del = list(input()) # 문자열은 리스트랑 다르게 수정이 안됩니다

for _ in range(N):
    for i in range(len(bef_del)):
        if bef_del[i] == '0':
            bef_del[i] = '1'
        else :
           bef_del[i] = '0' 

aft_del = list(input())
if aft_del == bef_del:
    print("Deletion succeeded")
else:
    print("Deletion failed")