'''
골5
시간제한 : 1초
메모리제한 : 256mb

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴
N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태

입력 : 
N (3의 거듭제곱. 3,9,27, ... 어떤 정수 k에 대해 N=3^k이며, 이때 1 ≤ k < 8)

출력 : 
첫째 줄부터 N번째 줄까지 별 출력
-> 재귀
'''
n = int(input())

graph = [[' ' for _ in range(n)] for _ in range(n)]
def star(n):
    
    if n == 3:
        graph[1] = ['*', ' ', '*']
        graph[0][:3] = graph[2][:3] = ['*'] * 3
        return
    
    star(n // 3)

    for i in range(0, n, n//3):
        for j in range(0, n, n//3):
            if i != n//3 or j != n//3:
                for k in range(n//3):
                    graph[i+k][j:j+n//3] = graph[k][:n//3]

star(n)

for i in range(n):
    for j in range(n):
        print(graph[i][j], end = '')
    print()

