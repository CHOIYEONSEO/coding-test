import sys

N = int(input())
new_list = []

for i in range(N):
    new_list.append(int(sys.stdin.readline()))

for i in range(N):
    min_num = min(new_list)
    print(min_num)
    new_list.remove(min_num)

# 메모리 초과