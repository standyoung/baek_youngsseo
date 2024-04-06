generator = []
all = []

for n in range(10000):
    all.append(n)
    split_n = n + sum(map(int, str(n)))  # 쪼개주기
    generator.append(split_n)

ans = list(set(all)-set(generator))
ans.sort()
print(*ans, sep="\n")