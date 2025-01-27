'''
시간제한 : 1초
메모리제한 : 1024mb

ax + by = c
dx + ey = f
연락방정식에서 x와 y 값 계산하기

입력 :
a, b, c, d, e, f 공백 구분
-999 <= a,b,c,d,e,f <= 999
x,y가 유일하게 존재. 
x y가 각각 -999 이상 999 이하의 정수인 경우만 입력으로 주어짐이 보장

출력 : 
x y 공백 구분 출력
-> 브루트포스
'''
import sys
input = sys.stdin.readline

a,b,c,d,e,f = map(int, input().rstrip().split())


for i in range(-999, 1000):
    for j in range(-999, 1000):
        if a * i + b * j == c:
            if d * i + e * j == f:
                print(i, j)
                break