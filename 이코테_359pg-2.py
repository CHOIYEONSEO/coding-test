import sys
input = sys.stdin.readline

n = int(input().rstrip())

students = []
for _ in range(n):
  name, kr, eng, math = input().rstrip().split()
  students.append((name, int(kr), int(eng), int(math)))

students.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in range(n):
  print(students[i][0])