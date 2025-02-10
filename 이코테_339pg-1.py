'''
시간제한 : 2초
메모리제한 : 256메가

입력 : 
n, m, k, x : 도시의 개수 / 도로의 개수 / 목표한 최단 거리 / 출발 도시 번호 (2 <= n <= 300,000 / 1 <= m <= 1,000,000 / 1 <= k <= 300,000 / 1 <= x <= n)
( m개의 줄에 )
a, b : a번 도시에서 b번 도시로 이동하는 단방향 도로 존재. (1 <= a, b <= n)

출력 : 
x로부터 출발해 도달할 수 있는 도시 중, 최단 거리가 k인 모든 도시 번호를 한 줄에 하나씩 오름차순으로 출력. 최단 거리가 k인 도시가 하나도 존재하지 않으면 !!! -1 !!! 출력.

* 출발도시 x에서 x로 가는 최단거리는 항상 0.
* a와 b는 서로 다른 자연수로 주어짐.
* 단방향 도로
* 출력할 때는 한 줄에 하나씩 오름차순 출력.
* 없으면 -1 출력.
'''
'''
시간초과 코드
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().rstrip().split())

graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)

distance = [INF] * (n+1)
def dikstra(start):
    q = []

    distance[start] = 0

    for e in graph[start]:
        heapq.heappush(q, (1, e))

    while q:
        cost, node = heapq.heappop(q)

        for e in graph[node]:
            heapq.heappush(q, (cost + 1 , e))
        
        distance[node] = min(distance[node], cost)

dikstra(x)

if distance.count(k) == 0:
    print(-1)

else:
    for i in range(len(distance)):
        if distance[i] == k:
            print(i)

-> 이미 방문한 노드도 전부 heapq에 넣어서 또 불필요하게 방문하고 있었음.
'''
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().rstrip().split())

graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)

distance = [INF] * (n+1)
def dikstra(start):
    q = []

    distance[start] = 0

    for e in graph[start]:
        heapq.heappush(q, (1, e))

    while q:
        cost, node = heapq.heappop(q)

        if distance[node] == INF:
            for e in graph[node]:
                heapq.heappush(q, (cost + 1 , e))
        
            distance[node] = cost

dikstra(x)

if distance.count(k) == 0:
    print(-1)

else:
    for i in range(len(distance)):
        if distance[i] == k:
            print(i)