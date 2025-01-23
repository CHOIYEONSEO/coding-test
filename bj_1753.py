'''
시간제한 : 1초
메모리제한 : 256mb

* 입력
V E (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000)
K : 시작 정점 번호(1 ≤ K ≤ V)
셋째 줄부터 E개의 줄에 걸쳐
u, v, w (u에서 v로 가는 가중치 w인 간선이 존재) w는 10 이하의 자연수

* 출력
시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력
i번 정점으로의 최단 경로의 경로값을 출력

주어진 시작점 -> 다른 모든 정점으로의 최단 경로
=> 다익스트라
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().rstrip().split())
k = int(input().rstrip())

graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))

distance = [INF] * (v+1)

def dijkstra(start):
    q = []

    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]: # (2,2) (3,3)
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])