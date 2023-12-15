import sys

# 8진수 변환
octal = int(sys.stdin.readline().rstrip(), 8)

# 8진수 2진수로 변환
print(bin(octal)[2:])
