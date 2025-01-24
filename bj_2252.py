'''
시간제한 : 2초
메모리제한 : 128mb

* 입력
첫째 줄에 N(1 ≤ N ≤ 32,000), M(1 ≤ M ≤ 100,000) / 학생들 번호 1번부터 N번, M은 키를 비교한 횟수
M개의 줄에는 키를 비교한 두 학생의 번호 A, B / 학생 A가 학생 B의 앞에 서야 한다는 의미

* 출력
첫째 줄에 학생들을 앞에서부터 줄을 세운 결과 출력
답이 여러 가지인 경우 아무거나 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
degree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    degree[b] += 1

q = deque()

for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)

result = []

while q:
    a = q.popleft()
    result.append(a)

    for x in graph[a]:
        degree[x] -= 1
        if degree[x] == 0:
            q.append(x)

print(*result)