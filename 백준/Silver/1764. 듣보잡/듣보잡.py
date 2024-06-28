import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

n_lst = set([sys.stdin.readline().rstrip() for _ in range(n)])
m_lst = set([sys.stdin.readline().rstrip() for _ in range(m)])

lst = list(m_lst.intersection(n_lst))

print(len(lst))
print(*sorted(lst), sep="\n")
