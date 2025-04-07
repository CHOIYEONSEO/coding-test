import sys
import math
input = sys.stdin.readline

n = int(input().strip())
students = list(map(int, input().rstrip().split(' ')))
b, c = map(int, input().rstrip().split(' '))

answer = len(students)
students = [(i - b) if (i - b) >= 0 else 0 for i in students]

for stu in students:
  answer += math.ceil(stu / c)

print(answer)