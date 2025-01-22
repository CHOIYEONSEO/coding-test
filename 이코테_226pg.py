'''
시간제한 1초
메모리제한 128MB

입력 :
n, m (1 <= n <= 100, 1 <= m <= 10,000)
n개의 줄에 각 화폐의 가치 (1 <= 화폐 가치 <= 10,000. 자연수)

출력 : 
m원을 만들기 위한 최소한의 화폐 개수
불가능할 때는 -1

n가지 종류 화폐. 최소한의 화폐 개수로 그 가치 합이 m원이 되도록 하려 함.
화폐 구성은 같지만 순서 다른 것은 같은 경우로 구분.
=> 바텀업 다이나믹 프로그래밍
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

money = []
for _ in range(n):
    money.append(int(input().rstrip()))
money.sort()

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(money[i], m+1):
        if d[j - money[i]] != 10001:
            d[j] = min(d[j], d[j - money[i]] + 1)

if d[m] == 10001:
    print(-1)

else:
    print(d[m])
