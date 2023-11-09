a, b, c = map(int, input().split())

lst = [a, b, c]
lst.sort()

if lst[2] < lst[0] + lst[1]:
    print(sum(lst))
else:
    print(2 * (lst[0] + lst[1]) - 1)
    # https://ko.wikipedia.org/wiki/%EC%82%BC%EA%B0%81%ED%98%95
