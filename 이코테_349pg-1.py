'''
시간제한 : 2초
메모리제한 : 512mb

입력
n : 수의 개수 (2<= n <=11)
a1, ..., an : 주어진 수 (1 <= ai <= 100)
x, y, z, q : 덧셈의 개수 / 뺄셈의 개수 / 곱셈의 개수 / 나눗셈의 개수 (합 n-1, 1<= n-1 <=10)

출력
만들 수 있는 식의 결과의 최댓값 (-10억 <= 최댓값, 최솟값 <= 10억)
만들 수 있는 식의 결과의 최솟값

* 주어진 수의 순서를 바꾸면 안됨
* 식의 계산은 연산자 우선순위 무시하고 앞에서부터 진행
* 나눗셈은 정수 나눗셈으로 몫만 취급.
* 음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꿈.
n이 11, 연산자 개수가 총 10이면 -> 10! / 4!*4! = 10*9*4*7*5
-> 브루트포스
'''
import sys
from itertools import permutations
input = sys.stdin.readline
INF = (1e9+1)

n = int(input().rstrip())
num = list(map(int, input().rstrip().split()))
x, y, z, q = map(int, input().rstrip().split())

operation = []
def make_operation(num, op):
    for _ in range(num):
        operation.append(op)

make_operation(x, '+')
make_operation(y, '-')
make_operation(z, '*')
make_operation(q, '/')

combination = set(permutations(operation, n-1))

def calculation(number, operator):
    total = number[0]

    for i in range(len(operator)):
        if operator[i] == '+':
            total += number[i+1]
        elif operator[i] == '-':
            total -= number[i+1]
        elif operator[i] == '*':
            total *= number[i+1]
        else:
            if total < 0 and number[i+1] > 0:
                total = -(-total // number[i+1])
            else:
                total //= number[i+1]


    return total

max_num = -INF
min_num = INF

for combi in combination:
    temp = calculation(num, combi)

    max_num = max(max_num, temp)
    min_num = min(min_num, temp)

print(max_num)
print(min_num)