A, B = map(int, input().split())

list1 = [i for i in range(1, 47)]

temp = 0
result = 0

for i in range(list1): # 2/
    temp += len(list1[i]) # 3/
    if A > temp - i * 10 ** (len(i)-1) and A <= temp: # 1,3/
        result += i * (i - (A - (temp - i * 10 ** (len(i)-1))) + 1) # 2


print(result)
            
# 해결못함.
        