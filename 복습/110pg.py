'''
시간제한 : 1초
메모리제한 : 128mb

입력 :
n : 공간 크기 (1 <= n <= 100)
이동계획 : L / R / U / D (1 <= 이동횟수 <= 100)

출력 : 
여행가 A가 최종적으로 도착할 지점 좌표 x, y

-> 구현
'''
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y) 
