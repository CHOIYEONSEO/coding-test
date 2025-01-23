'''
시간제한 : 0.5초
메모리제한 : 128mb

* 입력
N (1 ≤ N ≤ 1,000)
M (1 ≤ M ≤ 100,000)
셋째줄부터 M+2줄까지
출발도시번호 도착치번호 버스비용
(0 <= 버스비용 < 100,000)
구하고자 하는 구간 출발점의 도시번호, 도착점의 도시번호

* 출력
출발 도시 ~ 도착도시 : 최소비용
=> 다익스트라 힙
도시가 정점, 버스가 간선
'''
import heapq
import sys
INF = int(1e9)

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b,c))

s, e = map(int, input().rstrip().split())

distance = [INF] * (n+1)

def dijkstra(start):
    q = []

    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(s)

print(distance[e])