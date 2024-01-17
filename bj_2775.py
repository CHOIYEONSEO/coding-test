import sys

T = int(input())
new_arr = []

def count_num(a, b):
    new_arr = [[0 for col in range(b+1)] for row in range(a+1)]

    for i in range(1, b+1):
        new_arr[0][i] = i
    for i in range(1, a+1):
        for j in range(1, b+1):
            new_arr[i][j] = new_arr[i-1][j] + new_arr[i][j-1]

    return new_arr[a][b]

for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    print(count_num(k, n))