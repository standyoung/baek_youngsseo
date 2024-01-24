import sys
n = int(input())
age_lst = []  # 나이 정렬 리스트
dic = {}

for _ in range(n):
    inpt = sys.stdin.readline().rstrip().split()
    age = int(inpt[0])
    age_lst.append(age)

    if age not in dic:
        dic[age] = [inpt[1]]  # ["김성규"]

    else:  # 딕셔너리에 있다면
        dic[age].append(inpt[1])  # ["김성규", "장동우"]

age_lst = list(set(age_lst))
age_lst.sort()

for i in range(len(age_lst)):
    if len(dic[age_lst[i]]) == 1:
        print(age_lst[i], *dic[age_lst[i]])
    else:
        for j in range(len(dic[age_lst[i]])):
            print(age_lst[i], dic[age_lst[i]][j])

# lst = [0, 0, 0, "김성규"]
# lst[3] = [lst[3]]
# lst[3].append("장동우")
# print(lst)
# print(len(lst[3][0]) > 2)

# lst = [0, 0, 0, ["김성규", "장동우"]]
# lst[3].append("이성종")
# print(lst)
# print(len(lst[3][0]) > 2)

# dic = {10: ["김성규", "장동우"], 15: ["이성종"]}
# print(dic.get(10))
