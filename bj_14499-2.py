import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().rstrip().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().rstrip().split())))

moves = list(map(int, input().rstrip().split()))

#      동 서 남 북   # 바닥 6, 위 1
dx = [0, 0, -1, 1] # 바닥 3, 위 4 / 바닥 4, 위 3 / 바닥 5, 위 2 / 바닥 2, 위 5
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

def roll(move):
  if move == 1:
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2] # 주사위 변화 4 2 1 6 5 3
  elif move == 2: # 서쪽으로 굴리면
      dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3] # 주사위 변화 3 2 6 1 5 4
  elif move == 3: # 북쪽으로 굴리면
      dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1] # 주사위 변화 5 1 3 4 6 2
  elif move == 4: # 남쪽으로 굴리면
      dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4] # 주사위 변화 2 6 3 4 1 5

cur_top = 1
for move in moves:
  nx = x + dx[move-1]
  ny = y + dy[move-1]

  if 0 <= nx < n and 0 <= ny < m:
    x = nx
    y = ny
    
    roll(move)

    if graph[nx][ny] == 0:
      graph[nx][ny] = dice[5]

    else:
      dice[5] = graph[nx][ny]
      graph[nx][ny] = 0

    print(dice[0])

