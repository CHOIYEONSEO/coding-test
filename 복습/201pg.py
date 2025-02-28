'''
시간제한 : 2초
메모리제한 : 128mb

입력 : 
n, m : 떡의 개수, 요청한 떡의 길이 (1 <= n <= 1,000,000) (1 <= m <= 2,000,000,000)
떡의 개별 높이 n개 : (0 <= 높이 <= 1,000,000,000)

출력 : 
적어도 m만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값

* 떡 높이의 총합은 항상 M 이상이므로 손님은 필요한 양만큼 떡을 사갈 수 있음
-> 이진 탐색이자 파라메트릭 서치 유형
'''
n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    
    if total < m:
        end = mid - 1

    else:
        result = mid
        start = mid + 1

print(result)