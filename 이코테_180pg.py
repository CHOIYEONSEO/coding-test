'''
학생 이름, 성적 정보 -> 성적 기준 오름차순 정렬 -> 학생 이름 출력
=> key 기준 정렬라이브러리
'''
N = int(input())

student = []
for _ in range(N):
    name, score = input().split()
    student.append((name, int(score)))

def setting(data):
    return data[1]

student.sort(key = setting)

for i in range(N):
    print((student[i][0]), end = " ")
