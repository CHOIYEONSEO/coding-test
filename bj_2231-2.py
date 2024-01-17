N = int(input())
result = 0

for i in range(1, 7):
    if N >= (10**(i-1) + 1) and N <= ((10**i - 1) + 9 * i):
        for j in range(N - 9 * i, 10**i):
            result = j
            temp = j
            for k in range(i-1, -1, -1):
                result += (temp // (10 ** k))
                temp -= (temp // (10 ** k)) * (10 ** k)
            if result == N:
                result = j
                break
            else:
                result = 0

        if result != 0:
            break

print(result)

# 시간 : 40ms