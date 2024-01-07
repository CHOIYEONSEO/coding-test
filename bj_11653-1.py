N = int(input())
list = []

def factorization(a):
    num = 2
    while a > 1:
        if (a % num) == 0:
            list.append(num)
            factorization(a//num)
            break

        else:
            num += 1

factorization(N)
for i in range(len(list)):
    print(list[i])