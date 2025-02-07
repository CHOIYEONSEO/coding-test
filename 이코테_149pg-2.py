N, M = map(int, input().split())
board = []
result = 0

def dfs(graph, i, j):
    if graph[i][j] == 0:
        graph[i][j] = 1

        if i+1 < N:
            dfs(graph, i+1, j)

        if i-1 >= 0:
            dfs(graph, i-1, j)

        if j+1 < M:
            dfs(graph, i, j+1)

        if j-1 >= 0:
            dfs(graph, i, j-1)

        return 1

    return 0

for _ in range(N):
    board.append(list(map(int, input())))

for i in range(N):
    for j in range(M):
        result += dfs(board, i, j)

print(result)