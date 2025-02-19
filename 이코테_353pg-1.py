# 틀린 내 코드
'''
시간제한 : 2초
메모리제한 : 512mb

입력
n, l, r : 땅 크기 / 최소 인구 차이 / 최대 인구 차이 (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)
a1, ..., an : 인구 수 (0<= a1<= 100)

출력
인구 이동이 발생한 횟수

* 국경선을 공유하는 두 나라의 인구차가 l명 이상 r명 이하면, 인구 이동
* 이동후 인구수는 (연합인 모든 나라 인구수 합) / (연합을 이루고 있는 칸의 개수)
* 인구수 계산시 소수점은 버린다.
* 인구 이동이 발생하는 일수가 2000번 보다 작거나 같은 입력만 주어진다.
'''
import sys
input = sys.stdin.readline

n, l, r = map(int, input().strip().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().strip().split())))

def move():
    temp = []
    visit = [[False]*(n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j+1 < n and abs(data[i][j] - data[i][j+1]) >= l and abs(data[i][j] - data[i][j+1]) <= r:
                if visit[i][j] == False:
                    temp.append((i, j, data[i][j]))
                    visit[i][j] = True

                if visit[i][j+1] == False:
                    temp.append((i, j+1, data[i][j+1]))
                    visit[i][j+1] = True
            
            if i+1 < n and abs(data[i][j] - data[i+1][j]) >= l and abs(data[i][j] - data[i+1][j]) <= r:
                if visit[i][j] == False:
                    temp.append((i, j, data[i][j]))
                    visit[i][j] = True
                
                if visit[i+1][j] == False:
                    temp.append((i+1, j, data[i+1][j]))
                    visit[i+1][j] = True

    print(temp)
    union_len = len(temp)
    if union_len > 0:
        union_num = 0
        for x, y, z in temp:
            union_num += z

        new_num = union_num // union_len
        for x, y, z in temp:
            data[x][y] = new_num
        
        print(data)
        return True
    
    return False

count = 0

while move():
    count += 1

print(count)