import sys

N = int(input())
list = []

for i in range(N):
    list.append(int(sys.stdin.readline()))

list.sort()

for i in range(N):
    print(list[i])