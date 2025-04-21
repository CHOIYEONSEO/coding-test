import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
# print(n, k)
visited = [False] * (100001)

def bfs(visited):
    q = []
    heapq.heappush(q, (0, [n]))
    visited[n] = True

    while q:
        count, path = heapq.heappop(q)
        x = path[-1]
        if x == k:
            return count, path
        
        nx = 2*x
        if 0 <= nx <= 100000 and not visited[nx]:
            heapq.heappush(q, (count+1, path + [nx]))
            visited[nx] = True
        
        nx = x+1
        if 0 <= nx <= 100000 and not visited[nx]:
            heapq.heappush(q, (count+1, path + [nx]))
            visited[nx] = True

        nx = x-1
        if 0 <= nx <= 100000 and not visited[nx]:
            heapq.heappush(q, (count+1, path + [nx]))
            visited[nx] = True

if k < n:
    cnt = n - k
    answer = [i for i in range(n, k-1, -1)]
else:
    cnt, answer = bfs(visited)
print(cnt)
print(' '.join(list(map(str, answer))))