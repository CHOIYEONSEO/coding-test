N, M, K = map(int, input().split())
number_list = list(map(int, input().split()))

number_list.sort()

first_num = number_list[-1]
second_num = number_list[-2]

result = (M // (K + 1) * K + M % (K + 1)) * first_num
result += M // (K + 1) * second_num

print(result)