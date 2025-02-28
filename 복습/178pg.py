'''
시간제한 : 1초
메모리제한 : 128mb

입력 :
n : 수열에 속해 있는 수의 개수 (1 <= n <= 500)
(n개의 줄에)
자연수 : (1 <= 자연수 <= 100,000)

출력 :
내림차순 정렬 결과
-> 정렬
'''
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end = ' ')