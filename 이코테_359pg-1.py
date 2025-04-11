'''
시간제한 : 1초
메모리제한 : 256mb

입력 : 
n : 도현이네 반 학생 수 (1 <= n <= 100,000)
(n개의 줄에)
name, kor, eng, mat : 학생이름 / 국어 점수 / 영어 점수 / 수학 점수

출력 :
정렬 된 순서로 한 줄 씩 각 학생 이름 출력

* 국어 점수가 감소하는 순서로
* 국어 점수가 같으면 영어 점수가 증가하는 순서로
* 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
* 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 
* 대문자는 소문자보다 아스키코드에서 작으므로 사전 순으로 앞에 온다
'''
import sys
input = sys.stdin.readline

n = int(input().rstrip())
students = []
for _ in range(n):
    students.append(input().rstrip().split())

students.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))


for stu in students:
    print(stu[0])
    
