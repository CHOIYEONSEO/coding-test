'''
제각각 길이 K개
최대 랜선의 길이 구하기

첫째 줄에는 오영식이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력
K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수
항상 K ≦ N
랜선의 길이는 231-1보다 작거나 같은 자연수
-> 이진탐색, 파라메트릭 서치 유형
'''
import sys
input = sys.stdin.readline

k, n = map(int, input().rstrip().split())

h = []
for _ in range(k):
    h.append(int(input().rstrip()))

start = 1
end = max(h)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in h:
        total += x // mid

    if total >= n:
        result = mid
        start = mid + 1

    else:
        end = mid - 1

print(result)

