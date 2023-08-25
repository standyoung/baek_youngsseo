# 크로아티아 알파벳
# 크로아티아 알파벳이 몇 개로 이루어졌는지 출력하는 문제
# 특수 알파벳에 해당하면 교체하고 문자열의 길이를 측정하면 됨
# 만약 입력이 cc=이고 바꾸는 문자가 (공백)이면 c로 교체되어 1이 잘못 출력됨

c_lst = ['c-','c=','dz=','d-','lj','nj','s=','z=']

strr = input()

for i in c_lst:
    strr = strr.replace(i, "#")
print(len(strr))

# while문과 find()를 이용해서도 풀어보기