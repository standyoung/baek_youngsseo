slogan = "WelcomeToSMUPC"

N = int(input())

N = N % len(slogan)  # 14

print(slogan[N - 1])  # 몇 번째 => -1 인덱스