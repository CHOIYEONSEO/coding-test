'''
시간제한 2초
메모리제한 256MB

입력
n (1 <= n <= 500,000)
숫자 카드에 적혀있는 정수 공백으로 구분되어 입력 
(숫자 카드에 적혀있는 수 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.,
두 숫자 카드에 같은 수 적혀있는 경우 없음)
m (1 ≤ M ≤ 500,000)
상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야할 m개의 정수 공백으로 구분.
(-10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다)

출력
m개의 정수를 기준으로, 상근이가 가지고 있으면 1, 아니면 0을 공백으로 구분해 출력

=> 이진탐색
'''
import sys
input = sys.stdin.readline

n = int(input().rstrip())
have = list(map(int, input().rstrip().split()))
m = int(input().rstrip())
compare = list(map(int, input().rstrip().split()))

have.sort()
result = []

def binary_search(start, end, have):
    while (start <= end):
        mid = (start + end) // 2

        if num < have[mid]:
            end = mid - 1

        elif num > have[mid]:
            start = mid + 1

        else:
            return result.append(1)
    
    return result.append(0)


for num in compare:
    binary_search(0, n-1, have)

print(" ".join(map(str,result)))