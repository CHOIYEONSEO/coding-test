'''
시간제한 : 1초
메모리제한 : 128mb

입력 : 
n, m : 전체 회사 개수 / 경로 개수 (1 <= n,m <= 100)
(m개의 줄에)
연결된 두 회사의 번호
x, k : 최종 목적지, 중간에 방문해야하는 회사 (1 <= k <= 100)

출력 : 
k번 회사를 거쳐 x번 회사로 가는 최소 이동 시간. 도달할 수 없으면 -1 출력
'''
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b :
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")

else:
    print(distance)