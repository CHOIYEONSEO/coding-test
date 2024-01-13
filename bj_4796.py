import sys

case = 1

while True:
    L, P, V = map(int, sys.stdin.readline().split())
    result = 0

    if L == 0 and P == 0 and V == 0:
        break
    else:
        result = result + L * (V // P)
        temp = V - (P * (V // P))
        if temp <= L:
            result += temp
        else:
            result += L

        print("Case %d: %d" % (case, result))
        case += 1