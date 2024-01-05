import sys

N = int(input())
new_list = []

for i in range(N):
    new_list.append(int(sys.stdin.readline()))

new_list.sort()

for i in range(N):
    print(new_list[i])

# 메모리 초과