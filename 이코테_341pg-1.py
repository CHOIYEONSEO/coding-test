# 복습
'''
시간제한 : 2초
메모리제한 : 512메가

입력 : 
n, m : 지도 세로 크기 / 가로 크기 (3 <= n,m <= 8)
( n개의 줄에 )
a1, ..., am : 지도의 모양 ()

출력 : 
벽 3개를 세운 뒤 얻을 수 있는 안전 영역의 최대 크기

* 지도에서 0은 빈칸, 1은 벽, 2는 바이러스가 있는 위치다.
* 바이러스가 있는 위치의 개수(2의 개수)는 2보다 크거나 같고, 10보다 작거나 같은 자연수다.
* 빈칸의 개수(0의 개수)는 3개 이상이다.
* 바이러스는 상하좌우 인접한 빈칸으로 모두 퍼져나간다.
* 벽은 반드시 3개를 세운다.
* 안전영역은 벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 말한다.
-> dfs
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

board = []
for _ in range(n):
   board.append(list(map(int, input().rstrip().split())))

temp = [[0] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def get_score():
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1

    return count

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

result = 0

# temp 에 벽을 3개 세우는 모든 조합 찾기
def dfs(count):
    global result
    
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = board[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j) # 바이러스 확산

        result = max(result, get_score())
        return
         
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                count += 1
                dfs(count)
                board[i][j] = 0
                count -= 1

dfs(0)
print(result)