'''
시간제한 : 2초
메모리제한 : 128mb

입력 : 
n, m : 학생들 n번까지의 번호 / 수행할 수 있는 연산 개수 (1 <= n,m <= 100,000)
(m개의 줄에)
0|1 a b: 0은 팀 합치기 연산, 1은 같은 팀 여부 확인 연산 / a번학생 / b번학생 (1 <= a,b <= n)

출력 : 
같은 팀여부 확인 연산에 대하여 YES 혹은 NO 출력
'''
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int, input().split())
parent = [0] * (n+1)

for i in range(0, n+1):
    parent[i] = i

for i in range(m):
    oper, a, b = map(int, input().split())

    if oper == 0:
        union_parent(parent, a, b)

    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')

        else:
            print('NO')