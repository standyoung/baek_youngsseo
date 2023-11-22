num_list = list(map(int, input().split()))
if sorted(num_list) == num_list:
    print("ascending")
elif sorted(num_list, reverse=True) == num_list:
    print("descending")
else:
    print("mixed")