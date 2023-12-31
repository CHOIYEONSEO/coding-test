n = int(input())

new_list = []

while True:
    n, b = divmod(n, 2)
    if n >= 1:
        new_list.append(b)
    else:
        new_list.append(b)
        break

new_list.reverse()

print(''.join(map(str, new_list)))