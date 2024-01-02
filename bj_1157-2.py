word_input = input()
value_list = []
key_list = []
count_list = []

word_input = word_input.upper()

if len(word_input) == 1:
    print(word_input)

else:
    for i in range(len(word_input)):
        value_list.append(word_input[i])
        if word_input[i] in key_list:
            pass
        else:
            key_list.append(word_input[i])
    for i in range(len(key_list)):
        count_list.append(word_input.count(key_list[i]))

    count_list2 = count_list.copy()
    count_list.sort()
    if count_list[-1] == count_list[-2]:
        print("?")
    else:
        count_index = count_list2.index(count_list[-1])
        print(key_list[count_index])

# 런타임 에러