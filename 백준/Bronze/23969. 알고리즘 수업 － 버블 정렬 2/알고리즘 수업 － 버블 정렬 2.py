import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0
result = -1

for i in range(n-1,0,-1):
    for j in range(0,i,1):
        if array[j] > array[j+1]:
            cnt += 1
            array[j], array[j+1] = array[j+1], array[j]

            if cnt == k:
                print(*array, sep=" ")
                exit(0)
print(result)