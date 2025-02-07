'''
프로그래머스 18406
시간 제한: 1초
메모리 제한: 256메가바이트

입력 : 
n : 점수 (정수, 10 <= n <= 99,999,999, 자릿수는 항상 짝수 형태)

출력 : 
LUCKY / READY : 럭키 스트레이트 사용할수 있으면 / 사용할 수 없으면

* 점수를 반으로 나눠 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일하면 필살기 사용 가능
-> 구현
'''
n = input().rstrip()

numlen = len(n)

left = list(map(int, n[:numlen//2]))
right = list(map(int, n[numlen//2:]))

if sum(left) == sum(right):
    print('LUCKY')

else:
    print('READY')