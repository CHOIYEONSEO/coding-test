'''
시간제한 : 1초
메모리제한 : 512mb

입력 : 
n, m : 도시 크기 / 도시에 있는 치킨집 중 남길 수 있는 최대 개수 (2 ≤ N ≤ 50) (1 ≤ M ≤ 13)
( n개의 줄에 )
a1, ..., an : 도시 정보 (1 <= 집의 개수 <= 2n, m <= 치킨집 개수 <= 13)

출력 : 
도시의 치킨 거리의 최솟값

* 집 위치 (r1, c1)과 치킨집 위치 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|
* 도시 정보 3종류. 0 = 빈칸, 1 = 집, 2 = 치킨집
-> bfs
'''
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))

chicken = []
home = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i+1, j+1))

        if graph[i][j] == 1:
            home.append((i+1, j+1))


def distance(x, y):
    r1, c1 = x
    r2, c2 = y

    return abs(r1 - r2) + abs(c1 - c2)

def bfs():
    cost = []
    
    for i in range(len(chicken)):
        min_cost = INF
        for j in range(len(home)):
            min_cost = min(min_cost, distance(chicken[i], home[j]))
        
        if i >= m:
            if min_cost < cost[-1]:
                cost.pop()
                cost.append(min_cost)
                cost.sort()

        else:
            cost.append(min_cost)
            cost.sort()

    print(cost)
    return sum(cost)

print(bfs())