'''
시간제한 : 2초
메모리제한 : 512mb

* 입력
n, k (정수)
n : 수빈이가 있는 위치 (0 ≤ N ≤ 100,000)
k : 동생이 있는 위치 (0 ≤ K ≤ 100,000)

* 출력
수빈이가 동생을 찾는 가장 빠른 시간

걷는다면 1초 후 x-1 또는 x+1로 이동
순간이동하면 0초 후 2*x로 이동

=> 큐 다익스트라
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().rstrip().split())

distance = [INF] * (100001)

def dijkstra(start):
    q = []

    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        
        cost = dist + 0
        if 2 * now <= 100000 and cost < distance[2 * now]:
            distance[2 * now] = cost
            heapq.heappush(q, (cost, 2 * now))

        cost = dist + 1
        if now - 1 >= 0 and cost < distance[now - 1]: 
            distance[now - 1] = cost
            heapq.heappush(q, (cost, now - 1))

        if now + 1 <= 100000 and cost < distance[now + 1]:
            distance[now + 1] = cost
            heapq.heappush(q, (cost, now + 1))

    return distance[k]
            
print(dijkstra(n))