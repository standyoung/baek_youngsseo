# sort()와 sorted()의 차이점을 알아둘것..!
import sys
N = int(sys.stdin.readline())
num_lst = []

for _ in range(N):
    inpt = int(sys.stdin.readline())
    num_lst.append(inpt)

num_lst.sort()

print(*num_lst, sep='\n')