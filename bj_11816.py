input_x = input()
result = 0

if input_x[0] == '0':
    if input_x[1] == 'x':
        # 16진수
        input_x = input_x[2:]
        for i in range(len(input_x)):
            if input_x[i] == 'a':
                temp = 10
            elif input_x[i] == 'b':
                temp = 11
            elif input_x[i] == 'c':
                temp = 12
            elif input_x[i] == 'd':
                temp = 13
            elif input_x[i] == 'e':
                temp = 14
            elif input_x[i] == 'f':
                temp = 15
            elif input_x[i] == '1':
                temp = 1
            elif input_x[i] == '2':
                temp = 2
            elif input_x[i] == '3':
                temp = 3
            elif input_x[i] == '4':
                temp = 4
            elif input_x[i] == '5':
                temp = 5
            elif input_x[i] == '6':
                temp = 6
            elif input_x[i] == '7':
                temp = 7
            elif input_x[i] == '8':
                temp = 8
            elif input_x[i] == '9':
                temp = 9
            elif input_x[i] == '0':
                temp = 0
                
            result += pow(16, len(input_x)-i-1) * temp
    else:
        # 8진수
        input_x = input_x[1:]
        for i in range(len(input_x)):
            temp = int(input_x[i])
            result += pow(8, len(input_x)-i-1) * temp
else:
    # 10진수
    result = input_x

print(result)