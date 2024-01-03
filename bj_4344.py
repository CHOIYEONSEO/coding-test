C = int(input())

for i in range(C):
    new_list = list(map(int, input().split()))
    
    temp = new_list[0]
    sum = 0

    for j in range(1, temp+1):
        sum += new_list[j]

    average = sum / temp

    num = 0
    for j in range(1, temp+1):
        if new_list[j] > average:
            num += 1

    result = round(num/temp, 5) * 100

    print("%0.3f%%" % result)