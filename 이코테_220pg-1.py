'''
시간제한 1초
메모리 제한 128MB

입력
n (3 <= n <= 100)
k가 n개 공백으로 구분되어 (0 <= k <= 1,000)
출력
개미 전사가 얻을 수 있는 식량의 최댓값

일직선상에 존재하는 식량창고 중 최소한 한 칸 이상 떨어진 식량창고 약탈해야 됨.

=> 버텀업 다이나믹 프로그래밍
'''
n = int(input())
store = list(map(int, input().split()))

d = [0] * (n+1)
d[1] = store[0]
d[2] = max(store[0], store[1])

for i in range(3, n+1):
    d[i] = max(d[i-1], d[i-2] + store[i-1])

print(d[n])