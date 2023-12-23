n, k = map(int, input().split())

x_lst = list(map(int, input().split()))
x_lst.sort(reverse=True)

print(x_lst[k-1])