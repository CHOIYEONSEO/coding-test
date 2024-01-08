import sys

T = int(input())

def gcd_function(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i


for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    result = gcd_function(A, B)

    print(result * (A // result) * (B // result))