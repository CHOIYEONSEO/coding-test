'''
시간제한 : 10초
메모리제한 : 128mb

입력:
n : 퀸 개수(1 <= n <= 15)

출력 : 
퀸 n개를 서로 공격할 수 없게 놓는 경우의 수

* 퀸은 8방향(상하좌우 + 대각선)으로 모두 원하는 칸 만큼 이동 가능
'''
from collections import deque
n = int(input())

result = 0

def process(visit, pos):
    x, y = pos
    
    for i in range(n):
        visit[x][i] = True
        visit[i][y] = True
    
    nx, ny = x, y
    while nx-1 >= 0 and ny-1 >= 0:
        nx -= 1
        ny -= 1
        visit[nx][ny] = True

    nx, ny = x, y
    while nx+1 < n and ny+1 < n:
        nx += 1
        ny += 1
        visit[nx][ny] = True

    nx, ny = x, y
    while nx-1 >= 0 and ny+1 < n:
        nx -= 1
        ny += 1
        visit[nx][ny] = True

    nx, ny = x, y
    while nx+1 < n and ny-1 >= 0:
        nx+=1
        ny-=1
        visit[nx][ny] = True

    print(visit)

def find_index(visit, x, q):
    for i in range(x, n):
        for j in range(n):
            if visit[i][j] == False:
                q.append((i, j))
'''
for i in range(n):
    visit = [[False] * (n) for _ in range(n)]
    q = deque()
    temp = 0

    q.append((0, i))

    while q:
        x, y = q.popleft()
        if visit[x][y] == False:
            print(x, y)
            temp += 1
            process(visit, (x, y))
            
            find_index(visit, x, q)

    if temp == n:
        result += 1

    print("result : ", result)

print(result)
'''           

#2
answer = 0
def back(visit, pos):
    x, y = pos
    
    for i in range(n):
        visit[x][i] = False
        visit[i][y] = False
    
    nx, ny = x, y
    while nx-1 >= 0 and ny-1 >= 0:
        nx -= 1
        ny -= 1
        visit[nx][ny] = False

    nx, ny = x, y
    while nx+1 < n and ny+1 < n:
        nx += 1
        ny += 1
        visit[nx][ny] = False

    nx, ny = x, y
    while nx-1 >= 0 and ny+1 < n:
        nx -= 1
        ny += 1
        visit[nx][ny] = False

    nx, ny = x, y
    while nx+1 < n and ny-1 >= 0:
        nx+=1
        ny-=1
        visit[nx][ny] = False

visit = [[False] * (n) for _ in range(n)]
def dfs(row):
    global answer
    if row == n:
        answer += 1
        return 
    
    for column in range(n):
        if not visit[row][column]:
            process(visit, (row, column))
            dfs(row+1)
            back(visit, (row, column))

dfs(0)
print(answer)
