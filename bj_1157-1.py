word_input = input()
value_list = []
key_dict = {}

word_input = word_input.upper()

if len(word_input) == 1:
    print(word_input)
    
else:
    for i in range(len(word_input)):
        value_list.append(word_input[i])
        if word_input[i] in key_dict.keys():
            pass
        else:
            key_dict[word_input[i]] = 0

    for k in key_dict.keys():
        key_dict[k] = value_list.count(k)

    count_list = list(key_dict.values())
    count_list.sort()
    if count_list[-1] == count_list[-2]:
        print("?")
    else:
        key_dict2 = {v:k for k,v in key_dict.items()}
        print(key_dict2.get(count_list[-1]))

# 런타임 에러