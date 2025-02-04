'''
시간 제한 : 2초
메모리 제한 : 128mb

입력 : 
n, m : 팀 마지막 번호(n+1개 팀 존재) / 연산 개수 (1 <= n,m <= 100,000)
m개 줄 : 각각의 연산
팀 합치기 연산 - 0 a b (a번 학생이 속한 팀과 b번 학생이 속한 팀 합친다는 의미)
같은 팀 여부 확인 - 1 a b (a번 학생과 b번 학생이 같은 팀에 속해 있는지 확인하는 연산)
(a, b는 n이하의 양의 정수)

출력 : 
같은 팀 여부 확인 연산에 대하여 한 줄에 하나씩 YES 혹은 NO

학생들에게 0번부터 N번까지의 번호 부여.
처음에는 모든 학생이 서로 다른 팀으로 구분되어, 총 n+1개의 팀 존재.
'팀 합치기 연산'과 '같은 팀 여부 확인 연산'
- 팀 합치기 : 두 팀을 합치는 연산
- 같은 팀 여부 확인 : 특정한 두 학생이 같은 팀에 속하는지 확인하는 연산
-> 크루스칼 알고리즘
'''
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

for _ in range(m):
    c, a, b = map(int, input().split())

    if c == 0:
        union(parent, a, b)

    if c == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')