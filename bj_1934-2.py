import sys

def function_lcm(a, b, temp, result):
    if a == 1 and b == 1:
        return result
    else:
        if a % temp != 0 and b % temp != 0:
            return function_lcm(a, b, temp+1, result)
        elif a % temp == 0 and b % temp != 0:
            result = result * temp
            return function_lcm(a//temp, b, temp, result)
        elif a % temp != 0 and b % temp == 0:
            result = result * temp
            return function_lcm(a, b // temp, temp, result)
        elif a % temp == 0 and b % temp == 0:
            result = result * temp
            return function_lcm(a // temp, b // temp, temp, result)

T = int(input())

for i in range(T):
    list = []
    A, B = map(int, sys.stdin.readline().split())
    print(function_lcm(A, B, 2, 1))

# 런타임에러(RecursionError)