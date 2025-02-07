'''
시간제한 1초
메모리제한 128mb

입력 : n m
n : 전체 회사 개수
m : 경로 개수
1 <= n,m <= 100

둘째줄 ~ m+1 : 공백으로 구분된 연결된 두 회사의 번호 ie. 1 2

m+2번째줄 : x k
1 <= k <= 100

출력 : 최소 이동시간 출력
x번 회사 도달할 수 없다면 -1 출력


1 ~ n번 회사
두회사 양방향 이동 가능
1만큼의 시간으로 이동.

1번 회사 -> k -> x번 회사
이동 시간 최소 시간 계산
'''
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(1, m+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

x, k = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []

    q.append((0, start))
    distance[start] = 0

    while q:
        dist, now = q.pop(0)


        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + 1

            if cost < distance[i]:
                distance[i] = cost
                q.append((cost, i))


    return distance

oneToK = dijkstra(1)
kToX = dijkstra(k)

if oneToK[k] == INF or kToX[x] == INF:
    print("-1")
else:
    print(oneToK[k] + kToX[x])
