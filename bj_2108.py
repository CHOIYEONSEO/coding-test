'''
N은 홀수, 절댓값 4000 안넘는 정수
1 <= N <= 500,000

산술평균 -> sum/N
중앙값 -> 정렬 후 중앙값
최빈값 -> 
범위 -> max - min
'''
import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))

n = len(numbers)
numbers.sort()

print(round(sum(numbers)/n))

print(numbers[n//2])

commonArr = Counter(numbers).most_common()
if len(commonArr) == 1:
    print(commonArr[0][0])

else:
    common1 = commonArr[0]
    common2 = commonArr[1]

    if common1[1] == common2[1]:
        print(common2[0])

    else: 
        print(common1[0])

print(numbers[-1] - numbers[0])
