current = input()

column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row = ['1', '2', '3', '4', '5', '6', '7', '8']

count = 0


if column.index(current[0]) + 2 <= 7:
    if row.index(current[1]) + 1 <= 7:
        count += 1
    if row.index(current[1]) - 1 >= 0:
        count += 1

if column.index(current[0]) - 2 >= 0:
    if row.index(current[1]) + 1 <= 7:
        count += 1
    if row.index(current[1]) - 1 >= 0:
        count += 1

if row.index(current[1]) + 2 <= 7:
    if column.index(current[0]) + 1 <= 7:
        count += 1
    if column.index(current[0]) - 1 >= 0:
        count += 1

if row.index(current[1]) - 2 >= 0:
    if column.index(current[0]) + 1 <= 7:
        count += 1
    if column.index(current[0]) - 1 >= 0:
        count += 1

print(count)