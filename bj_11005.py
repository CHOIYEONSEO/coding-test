N, B = map(int, input().split())

digits = ['0', '1', '2' ,'3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',
          'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']

list = []

while True:
    if N >= 1:
        a, b = divmod(N, B)
        if a < B:
            list.append(digits[b])
            if a != 0:
                list.append(digits[a])
            break
        else:
            list.append(digits[b])
            N = a
    else:
        break

list.reverse()

print(''.join(list))
