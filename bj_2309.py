list = []
new_list = []

for i in range(9):
    list.append(int(input()))

def function():
    for i in range(9):
        new_list = list.copy()
        height_sum = sum(new_list) - new_list[i]
        if height_sum > 100:
            new_list.remove(new_list[i])

            for j in range(8):
                height_sum -= new_list[j]
                if height_sum == 100:
                    new_list.remove(new_list[j])
                    return new_list
                else:
                    height_sum +=  new_list[j]
        else:
            height_sum +=  new_list[i]

new_list = function()

new_list.sort()

for i in range(7):
    print(new_list[i])