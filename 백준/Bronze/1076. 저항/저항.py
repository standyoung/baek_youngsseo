resistor_dict = {
    "black": ["0", 1],
    "brown": ["1", 10],
    "red": ["2", 100],
    "orange": ["3", 1000],
    "yellow": ["4", 10000],
    "green": ["5", 100000],
    "blue": ["6", 1000000],
    "violet": ["7", 10000000],
    "grey": ["8", 100000000],
    "white": ["9", 1000000000],
}

in_lst = []
for _ in range(3):
    in_lst.append(input())

print(
    int(resistor_dict[in_lst[0]][0] + resistor_dict[in_lst[1]][0])
    * resistor_dict[in_lst[2]][1]
)