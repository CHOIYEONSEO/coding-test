n = int(input())

list = []
list.append(0)
list.append(1)

while True:
    temp = len(list)
    if n == temp:
        print(list[n-1] + list[n-2])
        break
    else:
        list.append(list[temp-1] + list[temp-2])

# 메모리 초과