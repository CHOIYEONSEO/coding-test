def fibonacci(b):
    temp = 0
    list1 = [0]
    list1.append(1)
    list1.append(1)

    for i in range(3, b+1):
        list1.append(list1[i-1] + list1[i-2])
        temp += 1

    return temp, list1

n = int(input())

temp, list1 = fibonacci(n)

print(list1[-1], temp)