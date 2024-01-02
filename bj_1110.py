def make_two_digit(a):
    list = []
    if a < 10:
        list.append(0)
        list.append(a)
    else:
        list.append(a // 10)
        list.append(a % 10)
    return list

N = int(input())
default = N
cycle = 0

while True:
    two_digit = make_two_digit(N)
    temp = two_digit[0] + two_digit[1]

    temp_two_digit = make_two_digit(temp)
    N = two_digit[1]*10 + temp_two_digit[1]
    cycle += 1

    if N == default:
        print(cycle)
        break
