import sys
N = int(sys.stdin.readline()) # 멀티탭 개수
av_max = 0

for i in range(N):
    av_p = int(sys.stdin.readline())

    if i != N-1:
        av_max += av_p - 1
    else :
        av_max += av_p

print(av_max)