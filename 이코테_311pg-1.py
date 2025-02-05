'''
시간 제한 : 1초
메모리 제한 : 128메가바이트

입력 : 
n : 모험가 수 (1 <= n <= 100000)
[] : 각 모험가의 공포도 값 공백으로 구분 (n 이하 자연수)

출력 : 
여행을 떠날 수 있는 그룹 수의 최댓값

* 공포도가 X인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여
* 모든 모험가를 특정한 그룹에 넣을 필요는 없음. 몇 명의 모험가는 마을에 남아있어도 됨.
'''
# 틀린코드
n = int(input())
num = list(map(int, input().split()))

num.sort()

result = 0
i = 0
for j in range(n):
    if len(num[i:len(num)-j]) >= num[-1-i]:
        result += 1
        i += num[-1-i]-1
    
    else:
        break

print(result)