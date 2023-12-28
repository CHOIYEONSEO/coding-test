list = list()

for i in range(9):
    list.append(int(input()))
    
max = list[0]

for i in range(1, 9):
    if list[i] > max:
        max = list[i]

print(max)
print(list.index(max)+1)