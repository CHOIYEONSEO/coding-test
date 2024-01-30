N, M = map(int, input().split())

result = 0

for i in range(N):
    card_list = list(map(int, input().split()))

    min_num = min(card_list)
    result = max(min_num, result)

print(result)
