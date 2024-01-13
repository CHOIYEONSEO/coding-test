str1 = input()

result = 0

for i in range(len(str1)):
    result += (2 ** (len(str1) - i - 1)) * int(str1[i])

print("%o" % result)

# 시간 초과