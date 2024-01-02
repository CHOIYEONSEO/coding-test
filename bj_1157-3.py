word_input = input()
key_list = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, "X":0, "Y":0, "Z":0}

word_input = word_input.upper()

if len(word_input) == 1:
    print(word_input)

else:
    for k in key_list.keys():
        key_list[k] = word_input.count(k)

    max_list = [k for k,v in key_list.items() if max(key_list.values()) == v]

    if len(max_list) > 1:
        print("?")
    else:
        print(max_list[0])
