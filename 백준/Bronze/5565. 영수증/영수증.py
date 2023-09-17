total = int(input())
lst = []

for _ in range(9):
    book = int(input())
    lst.append(book)

print(total - sum(lst))