A, B = map(int, input().split())

list1 = [i for i in range(10001)]

temp = 0
result = 0

while True:
    i = 1
    temp += list1[i]
    if temp >= A:
        if B <= temp:
            result += list1[i] * (B - temp + list1[i])
            break
        else:
            result += list1[i] * (A - temp + list1[i])
            print(result)

print(result)
            

        