import sys

input = sys.stdin.readline

int(input())
i_set = set(map(int, input().split()))

int(input())
given_lst = list(map(int, input().split()))

for i in given_lst:
    if i in i_set:
        print(1, end=" ")
    else:
        print(0, end=" ")