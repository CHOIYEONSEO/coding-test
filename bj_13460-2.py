import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = []

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
q = deque()

rx, ry, bx, by = 0, 0, 0, 0

for i in range(n):
  for j in range(m):
    if board[i][j] == "R":
      rx, ry = i, j
    if board[i][j] == "B":
      bx, by = i, j

q.append([rx, ry, bx, by, 1])
visited.append([rx, ry, bx, by])

def move(x, y, i, j):
  count = 0
  while board[x+i][y+j] != "#" and board[x][y] != "O":
    x += i
    y += j
    count += 1

  return x, y, count

def bfs():
  while q:
    rx, ry, bx, by, cnt = q.popleft()

    if cnt > 10:
      break

    for i in range(4):
      nrx, nry, rCnt = move(rx, ry, dx[i], dy[i])
      nbx, nby, bCnt = move(bx, by, dx[i], dy[i])

      if board[nbx][nby] == "O":
        continue

      if board[nrx][nry] == "O":
        return cnt
      
      if nrx == nbx and nry == nby:
        if rCnt > bCnt:
          nrx -= dx[i]
          nry -= dy[i]

        else:
          nbx -= dx[i]
          nby -= dy[i]

      if [nrx, nry, nbx, nby] not in visited:
        visited.append([nrx, nry, nbx, nby])
        q.append([nrx, nry, nbx, nby, cnt+1])

  return -1

print(bfs())