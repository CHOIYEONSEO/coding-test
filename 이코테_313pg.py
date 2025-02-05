'''
시간 제한 : 2초
메모리 제한 : 128메가바이트

입력:
s : 0과 1로 이루어진 문자열 (s길이 < 100만)

출력:
해야하는 행동의 최소 횟수

* s에 있는 모든 숫자를 전부 같게 만들려고 함
* 한번의 행동에 s에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집을 수 있음
* 뒤집는다는 1을 0으로 0을 1로 바꾸는 것을 의미함
* ex. 0001100은 2번으로 1111111이 될 수 있지만, 1번으로 0000000이 될 수 있음.
-> 그리디
'''
s = input().rstrip()

toOne = 0
for i in range(len(s)):
    if len(s) == 1:
        toOne = 1
        break

    if i == len(s)-1:
        if s[i] == '0':
            toOne += 1
        break

    if s[i] == '0' and s[i] != s[i+1]:
        toOne += 1

toZero = 0
for i in range(len(s)):
    if len(s) == 1:
        toZero = 1
        break

    if i == len(s)-1:
        if s[i] == '1':
            toZero += 1
        break

    if s[i] == '1' and s[i] != s[i+1]:
        toZero += 1

print(min(toOne, toZero))