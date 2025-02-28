'''
시간제한 :  1초
메모리제한 : 128mb

입력 : 
n, m : 세로 / 가로 (1 <= n,m <= 1,000)
(n개의 줄에)
얼음 틀 형태 : 0은 뚫려있음. 1은 칸막이.

출력 : 
한번에 만들 수 있는 아이스크림 개수

-> dfs
'''
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)