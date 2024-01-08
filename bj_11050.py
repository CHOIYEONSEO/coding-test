N, K = map(int, input().split())

if K == 0:
    result = 1
else:
    result = N

for i in range(K-1):
    N = N - 1
    result = result * N

for i in range(K):
    result = result / K
    K = K - 1

print("%d" % result)