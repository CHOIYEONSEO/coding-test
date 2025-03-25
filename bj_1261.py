import heapq
import sys
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())

maze = []
for _ in range(n):
    maze.append(list(input().rstrip()))

# print(maze) #['011', '111', '110']

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, maze):
    q = []
    count = 0

    heapq.heappush(q, (count, x, y))
    maze[x][y] = '-1'
    # print(maze[x][y])

    while q:
        count, x, y = heapq.heappop(q)
        if x == n-1 and y == m-1:
            return count
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == '-1':
                    continue
                if maze[nx][ny] == '1':
                    heapq.heappush(q, (count+1, nx, ny))
                if maze[nx][ny] == '0':
                    heapq.heappush(q, (count, nx, ny))
                maze[nx][ny] = '-1'

print(bfs(0, 0, maze))