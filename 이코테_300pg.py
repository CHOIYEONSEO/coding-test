'''
시간 제한 : 2초
메모리 제한 : 256mb

입력 :
n, m : 집 개수 / 길 개수 (2 <= n <= 100,000, 1 <= m <= 1,000,000)
m개의 줄에 a, b, c : a번 집과 b번 집을 연결하는 길의 유지비 c (1 <= c <= 1,000)

출력 :
길 없애고 남은 유지비 합의 최솟값 출력

* 길 양방향
* 마을을 2개의 분리된 마을로 분할할 계획.
* 분리된 마을 내에는 집이 하나 이상 있어야 됨.
* 분리된 마을 내 집들이 서로 연결되도록.
* 분리된 두 마을 사이 길들은 없을 수 있음.
* 분리된 마을 안의 집들 최소신장트리로.
* 유지비가 최소가 되도록
-> 분리된 마을 안 집 유지비 합은 크루스칼
-> 크루스칼로 최소신장트리 만들고 가장 큰 유지비 간선 제거
-> 비용 기준 정렬
'''
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

result = 0
max_cost = 0
for i in range(m):
    cost, a, b = graph[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        max_cost = max(max_cost, cost)
        result += cost

print(result - max_cost)