N, m, M, T, R = map(int, input().split())

min_m = m
num = 0
result = 0

while True:
    if num == N:
        print(result)
        break
    elif (m + T) <= M :
        m = m + T
        num += 1
        result += 1
    else:
        m = m - R
        if m < min_m:
            m = min_m
            if (m + T) > M :
                print(-1)
                break
        result += 1