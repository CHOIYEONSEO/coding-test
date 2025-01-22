'''
시간제한 : 1초
메모리제한: 256mb

n : 정점 개수 (1 <= n <= 100)
i,j = 1이면 간선 존재.
i,j = 0이면 간선 없음.
i,i = 항상 0

모든 정점에 대해서 연결된걸 봐야하므로 -> 플로이드 워셜
'''
# 틀린 코드. 반례 찾아야 됨.

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input().rstrip())

graph = []

for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))

distance = [[INF] * (n) for _ in range(n)]

distance[0][0] = 0

for a in range(n):
    for b in range(n):
        if graph[a][b] == 1:
            distance[a][b] = 1

for k in range(n):
    for a in range(n):
        for b in range(n):
            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

    for j in range(n):
        if distance[i][j] == INF or distance[i][j] == 0:
            print("0", end = " ")
    
        else:
            print("1", end = " ")

    print()
