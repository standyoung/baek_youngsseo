import sys

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]

lst.sort()
# sort() : 기존 lst 오름차순으로 정렬
# sorted() : 기존 lst 냅두고 새롭게 정렬된 리스트로 반환

for i in range(len(lst)):
    print(lst[i])
# print(*lst, sep="\n")
# * : unpacking operator
# sep : 구분자