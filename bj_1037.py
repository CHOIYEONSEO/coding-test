import sys

num = int(input())

list = list(map(int, sys.stdin.readline().split()))

print(min(list) * max(list))