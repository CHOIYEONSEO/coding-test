import sys

def function_lcm(a, b, temp):
    if a == 1 and b == 1:
        return list
    else:
        if a % temp != 0 and b % temp != 0:
            return function_lcm(a, b, temp+1)
        elif a % temp == 0 and b % temp != 0:
            list.append(temp)
            return function_lcm(a//temp, b, temp)
        elif a % temp != 0 and b % temp == 0:
            list.append(temp)
            return function_lcm(a, b // temp, temp)
        elif a % temp == 0 and b % temp == 0:
            list.append(temp)
            return function_lcm(a // temp, b // temp, temp)

T = int(input())

for i in range(T):
    list = []
    A, B = map(int, sys.stdin.readline().split())
    list = function_lcm(A, B, 2)
    result = 1
    for i in range(len(list)):
        result = result * list[i]

    print(result)

# 런타임에러(RecursionError)