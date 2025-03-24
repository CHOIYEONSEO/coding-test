'''
입력
n, m : 보드의 세로 / 가로 (3 <= n, m <= 10)
(n개의 줄에)
길이 m의 문자열 : 보드 모양.
    - . : 빈칸
    - # : 장애물
    - O : 구멍 위치 (1개)
    - R : 빨간 구슬 위치 (1개)
    - B : 파란 구슬 위치 (1개)

출력
최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지. 10번 이하로 빼낼 수 없으면 -1 출력.

* 4가지 동작(왼쪽/오른쪽/위쪽/아래쪽 기울이기) 가능.
* 각각의 동작에서 빨간 구슬과 파른 구슬은 동시에 움직임.
* 빨간 구슬이 구멍에 빠지면 성공, 파란 구슬이 구멍에 빠지면 실패.
* 빨간 구슬과 파란 구슬 동시에 구멍에 빠져도 실패
* 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없음.
* 기울이는 동작은 그만하는 것은 더 이상 구슬이 움직이지 않을때 까지
* 입력되는 모든 보드의 가장자리는 '#'

-> DFS 
'''
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
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j

q.append([rx, ry, bx, by, 1])
visited.append([rx, ry, bx, by])

def move(x, y, i, j):
    count = 0
    while board[x+i][y+j] != '#' and board[x][y] != 'O':
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

            if board[nbx][nby] == 'O':
                continue

            if board[nrx][nry] == 'O':
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
