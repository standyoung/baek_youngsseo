m_k = list(map(int, input().split()))
m_s = list(map(int, input().split()))

sum_m_k = sum(m_k)
sum_m_s = sum(m_s)

if sum_m_k == sum_m_s:
    print(sum_m_k)

else:
    print(max(sum_m_k, sum_m_s))
