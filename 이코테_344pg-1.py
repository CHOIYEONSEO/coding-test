# 틀린 내 코드
'''
시간제한 : 1초
메모리제한 : 256메가

입력 :
n, k : 시험관 크기 / 바이러스 종류 (1 <= n <= 200, 1 <= k <= 1000)
( n개의 줄에 )
a1, ..., an : 시험관의 정보. (바이러스 존재하지 않으면 0) (ai는 k이하의 자연수)
s, x, y : 궁금한 몇 초 뒤 / 행 / 열 (0 <= s <= 10,000) (1 <= x,y <= n)

출력 : 
s초 뒤 (x, y)에 존재하는 바이러스 종류 출력. 만약 해당 위치에 바이러스가 존재하지 않는 다면 0 출력.

* 모든 바이러스는 1초마다 상, 하, 좌, 우 방향으로 증식함
* 매초 번호가 낮은 종류의 바이러스부터 먼저 증식함. 
* 특정 칸에 이미 바이러스가 있으면 그곳에는 다른 바이러스가 들어갈 수 없음
* (행=x, 열=y)은 (1, 1)에서 시작
-> dfs
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

info = []
for _ in range(n):
    info.append(list(map(int, input().rstrip().split())))

s, row, col = map(int, input().rstrip().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

temp = [[0] * n for _ in range(n)]

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if temp[nx][ny] == 0:
                temp[nx][ny] = info[x][y]
            else:
                temp[nx][ny] = min(info[x][y], temp[nx][ny])

def dfs():
    for i in range(n):
        for j in range(n):
            if info[i][j] != 0:
                virus(i, j)

    for i in range(n):
        for j in range(n):
            if info[i][j] == 0 and temp[i][j] != 0:
                info[i][j] = temp[i][j]

for _ in range(s):
    dfs()

print(info[row-1][col-1])