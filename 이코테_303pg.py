'''
시간 제한 : 2초
메모리 제한 : 128mb

입력 : 
n : 듣고자 하는 강의 수 (1 <= n <= 500)
n개의 줄에 a, (b..c), -1 : 강의 강의시간 / 선수과목 번호 / -1 (1 <= 강의 시간 <= 100,000) 

출력 :
n개의 강의에 대해 수강하기까지 걸리는 최소 시간 한 줄에 하나씩

* 동시에 여러 개 강의 들을 수 있음
* 10 -1 / 4 1 -1 / 3 2 -1 이면 3번째 강의는 시간 17 (7 x)

-> 선수과목 -> 위상정렬
'''
from collections import deque
import copy

n = int(input())
indegree = [0] * (n+1)

info = []
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)
for i in range(1, n+1):
    data = (list(map(int, input().split())))
    time[i] = data[0]

    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i) 

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()