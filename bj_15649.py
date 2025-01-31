'''
실3
시간제한 : 1초
메모리제한 : 512mb

입력 : 
n, m
(1 ≤ M ≤ N ≤ 8)

출력 : 
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력
수열은 사전 순으로 증가하는 순서로 출력

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
-> 백트랙킹
'''
n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False

dfs()