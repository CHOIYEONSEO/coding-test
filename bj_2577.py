a = int(input())
b = int(input())
c = int(input())

d = a * b * c
result_list = list()
d_len = len(str(d))

for i in range(d_len):
    result_list.append(d//(10**(d_len-i-1)))
    d -= result_list[i]*(10**(d_len-i-1))

for i in range(10):
    print(result_list.count(i))