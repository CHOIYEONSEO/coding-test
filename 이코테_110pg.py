N = int(input())
move_list = input().split()

result = [1, 1]

for i in range(len(move_list)):
    if move_list[i] == 'L':
        if result[1] > 1:
            result[1] -= 1

    elif move_list[i] == 'R':
        if result[1] < N:
            result[1] += 1

    elif move_list[i] == 'U':
        if result[0] > 1:
            result[0] -= 1

    elif move_list[i] == 'D':
        if result[0] < N:
            result[0] += 1

print(result[0], result[1])