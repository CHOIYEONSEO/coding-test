row, column = map(int, input().split())

map_list = [[i for i in range(column)] for j in range(row)]

position = list(map(int, input().split()))

for j in range(row):
    map_update = list(map(int, input().split()))

    for i in range(column):
        map_list[j][i] = map_update[i]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

count = 1

while True:
    if map_list[position[0]][position[1]] == 0:
        map_list[position[0]][position[1]] = 1
        count += 1

        while True:
            if map_list[position[0]+dx[position[2]]][position[1]+dy[position[2]]] == 0:
                position[0] += dx[position[2]]
                position[1] += dy[position[2]]
                map_list[position[0]][position[1]] = 1
                count += 1

                break

            if position[2] == 0:
                position[2] = 3
            else:
                position[2] -= 1
    
    else:
        break

print(count)
                
        




