new_list = list()
residual_list = list()

for i in range(10):
    new_list.append(int(input()))
    residual_list.append(new_list[i] % 42)

residual_list.sort()

num = 1

for i in range(9):
    if residual_list[i] != residual_list[i+1]:
        num += 1

print(num)
