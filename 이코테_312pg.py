'''
시간 제한 : 1초
메모리 제한 : 128메가바이트

입력 : 
s : 여러개의 숫자(0부터 9)로 구성된 하나의 문자열 (1 <= s길이 <= 20)

출력 : 
만들어질 수 있는 가장 큰 수

* 하나씩 숫자 확인하며 숫자 사이에 'x' 또는 '+' 연산자를 넣는다(숫자는 항상 일의자리)
* 계산은 왼쪽에서부터 순서대로 이루어진다고 가정
* 만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어짐
-> 그리디
'''
s = list(map(int,input().rstrip()))

result = s[0]
for i in range(len(s)-1):
    if result + s[i+1] > result * s[i+1]:
        result = result + s[i+1]

    else:
        result = result * s[i+1]

print(result)