""" 
단순 정렬 -> 정렬 라이브러리

1이상 100,000이하 자연수 내림차순 정렬
공백 구분 출력. 동일한 수 순서 자유
"""
N = int(input())
number = list()

for i in range(N):
    number.append(int(input()))

number.sort()
number.reverse()

#number.sort(reverse = True)

print(' '.join(map(str, number)))