strings = input()
flag = 0

for i in range(len(strings)):
    if strings[i] == 'A' or strings[i] == 'B' or strings[i] == 'C' :
        time = 3
        flag += time
    elif strings[i] == 'D' or strings[i] == 'E' or strings[i] == 'F' :
        time = 4
        flag += time
    elif strings[i] == 'G' or strings[i] == 'H' or strings[i] == 'I' :
        time = 5
        flag += time
    elif strings[i] == 'J' or strings[i] == 'K' or strings[i] == 'L' :
        time = 6
        flag += time
    elif strings[i] == 'M' or strings[i] == 'N' or strings[i] == 'O' :
        time = 7
        flag += time
    elif strings[i] == 'P' or strings[i] == 'Q' or strings[i] == 'R' or strings[i] == 'S' :
        time = 8
        flag += time
    elif strings[i] == 'T' or strings[i] == 'U' or strings[i] == 'V' :
        time = 9
        flag += time
    elif strings[i] == 'W' or strings[i] == 'X' or strings[i] == 'Y' or strings[i] == 'Z' :
        time = 10
        flag += time
        
print(flag)   