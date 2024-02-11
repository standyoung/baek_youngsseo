a, b = map(int, input().split())
lst = [0]
n = 1

while n != 100: # a,b가 1000을 넘지 않으니까 n을 100개 미만으로 해도 ㄱㅊ

    for i in range(n):
        lst.append(n)

    n += 1

print(sum(lst[a:b+1]))
