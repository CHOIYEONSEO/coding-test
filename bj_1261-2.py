import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

graph = []
for i in range(m):
  graph.append(list(input().rstrip()))
# graph = [['0']*100 for _ in range(100)]
# print(len(graph))

# print(graph)

visited = [[False] * n for _ in range(m)] 
# print(visited)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
  q = []
  heapq.heappush(q, (0, 0, 0))
  visited[0][0] = True

  while q:
    count, x, y = heapq.heappop(q)

    if x == m-1 and y == n-1:
      return count
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
        if graph[nx][ny] == '1':
          heapq.heappush(q, (count + 1, nx, ny))
          visited[nx][ny] = True
        
        else:
          heapq.heappush(q, (count, nx, ny))
          visited[nx][ny] = True

print(bfs())