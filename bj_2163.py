N, M = map(int, input().split())

temp = N * M
num = 0
while True:
    if temp == 1:
        print(num)
        break
    else:
        temp -= 1
        num += 1 

