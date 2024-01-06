import sys

N = int(input())
list = []

for i in range(N):
    list.append(int(sys.stdin.readline()))

list.sort()

for i in range(N):
    print(list[i])

# 시간제한 : 1초, 메모리 제한 : 128 MB
# 통과