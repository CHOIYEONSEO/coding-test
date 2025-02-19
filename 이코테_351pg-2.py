'''
시간제한 : 2초
메모리제한 : 256mb

입력
n : 복도 크기 (3 <= n <= 6)
( n개의 줄에 )
a1, ..., an : 복도의 정보

출력
정확히 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지 여부 (YES/NO)

* 선생님은 상, 하, 좌, 우 방향으로 감시
* 아무리 멀리 있어도 장애물로 막히기 전까지 4가지 방향으로 학생 모두 볼 수 있음
* 장애물 뒤편에 숨어 있는 학생은 볼 수 없음
* 복도 정보 : S = 학생, T = 선생님, 빈칸 = X.
* X의 개수는 항상 3개 이상
'''
import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input().rstrip())

board = []
teachers = []
spaces = []

for i in range(n):
    board.append(input().rstrip().split())

    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))

        elif board[i][j] == 'X':
            spaces.append((i, j))


def watch(x, y, direction):
    if direction == 0: # 상
        while y >= 0:
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
            y -= 1
        
    elif direction == 1: # 하
        while y < n:
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
            y += 1

    elif direction == 2: # 좌
        while x >= 0:
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
            x -= 1

    elif direction == 3: # 우
        while x < n:
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
            x += 1

    return False

def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True # 학생 만나면
    return False # 학생 안 만나면

find = False

for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y] = 'O'

    if not process():
        find = True
        break

    for x, y in data:
        board[x][y] = 'X'

if find:
    print("YES")
else:
    print("NO")