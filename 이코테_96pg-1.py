N, M = map(int, input().split())

result = 0

for i in range(N):
    card_list = list(map(int, input().split()))
    
    card_list.sort()

    if result == 0:
        result = card_list[0]
    elif result < card_list[0]:
        result = card_list[0]

print(result)