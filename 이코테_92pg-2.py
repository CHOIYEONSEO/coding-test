N, M, K = map(int, input().split())

number_list = list(map(int, input().split()))

number_list.sort()

result = 0
count = 0

first_num = number_list[-1]
second_num = number_list[-2]

while True:
    for i in range(K):
        if count == M:
            break
        result += first_num
        count += 1

    if count == M:
        break
    else:
        result += second_num
        count += 1

print(result)