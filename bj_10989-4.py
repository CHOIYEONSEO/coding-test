import sys

N = int(input())
new_list = [0 for i in range(100001)]

for i in range(N):
    temp = int(sys.stdin.readline())
    new_list[temp] += 1

for i in range(1, N+1):
    if new_list[i] > 0:
        for j in range(new_list[i]):
            print(i)

# 런타임 에러(IndexError)