import sys

N = int(input())

my_list = [sys.stdin.readline().strip() for i in range(N)]
temp = list(my_list[0])

for i in range(len(my_list[0])):
    for j in range(N-1):
        if my_list[j][i] != my_list[j+1][i]:
            temp[i] = '?'

print(''.join(temp))