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
dice = [0, 0, 0, 0, 0, 0, 0] # index 0 제외
top = [[0], [4, 3, 5, 2], [4, 3, 1, 6], [1, 6, 5, 2], [6, 1, 5, 2], [4, 3, 6, 1], [4, 3, 2, 5]] # index 0 제외
bottom = [0, 6, 5, 4, 3, 2, 1]

cur_top = 1
for move in moves:
  nx = x + dx[move-1]
  ny = y + dy[move-1]

  if 0 <= nx < n and 0 <= ny < m:
    x = nx
    y = ny
    cur_top = top[cur_top][move-1]
    if graph[nx][ny] == 0:
      graph[nx][ny] = dice[bottom[cur_top]]

    else:
      dice[bottom[cur_top]] = graph[nx][ny]
      graph[nx][ny] = 0
    print(dice)
    print(dice[cur_top])

