s1, s2, s3 = map(int, input().split())

sum_list = list()

for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            sum_list.append(i+j+k)

count_dict = {}

for i in range(3, s1+s2+s3+1):
    count_dict[i] = sum_list.count(i)

count_list = list(count_dict.values())

count_list.sort()
max_count = count_list[-1]


for k, v in count_dict.items():
    if v == max_count:
        print(k)
        break