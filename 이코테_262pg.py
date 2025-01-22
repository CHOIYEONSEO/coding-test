'''
입력
n m c
n: 도시 개수 (1 <= n <= 30,000)
m: 통로 개수 (1 <= m <= 200,000)
c: 메시지 보내고자 하는 도시 (1 <= c <= n)

2번째 줄 ~ m+1:
x y z
특정 도시 x에서 y 도시로 이어지는 통로가 있고, 메시지 전달되는 시간 z
(1 <= x,y <= n)
(1 <= z <= 1,000)

출력
도시 c에서 보낸 메시지 받는 도시 총 개수와 총 걸리는 시간 공백 구분 출력
ie. 2 4

단반향 통신
c에서 최대한 많은 도시로 메시지를 보내고자 함.
-> 다익스트라 힙(우선순위 큐) 사용
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().rstrip().split())

graph = [[] for i in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().rstrip().split())
    graph[x].append((y, z))

distance = [INF] * (n+1)

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
time = 0
for i in range(2, n+1):
    if distance[i] != INF:
        count += 1
        time = max(time, distance[i])

print(count, time)