'''
4 6
19 15 10 17
->
15

첫째 줄 : 떡 개수 N, 요청한 떡 길이 M (1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000)
둘째 줄 : 떡 개별 높이. 0 <= 높이 <= 10억

적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값 출력

-> 데이터 범위 크므로 이진탐색
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
height = list(map(int, input().rstrip().split()))

start = 0
end = max(height)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2

    for x in height:
        if x > mid:
            total += x - mid
        
    if total < M:
        end = mid - 1

    else:
        result = mid
        start = mid + 1

print(result)