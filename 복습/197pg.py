'''
시간제한 : 1초
메모리제한 : 128mb

입력 : 
n : 부품 개수 (1 <= n <= 1,000,000)
n개의 부품 고유 번호 : (1 < 정수 <= 1,000,000)
m : 문의한 부품 종류 개수 (1 <= m <= 100,000)
m개의 부품 번호 : (1 < 정수 <= 1,000,000)

출력 : 
각 부품이 존재하면 yes, 없으면 no 출력
-> 이진 탐색
'''
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')