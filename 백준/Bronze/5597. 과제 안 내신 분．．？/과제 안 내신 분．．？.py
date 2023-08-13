input_list = []
num_list = []

while True:
    a = int(input())
    input_list.append(a)
    if len(input_list) == 28:
        break

input_list = sorted(input_list)
for i in range(30):
    num_list.append(i+1)

for i in range(len(num_list)):
    if num_list[i] not in input_list:
        print(num_list[i])