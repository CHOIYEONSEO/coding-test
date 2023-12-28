a = int(input())
b = int(input())

num100 = b // 100
b = b - num100 * 100
num10 = b // 10
num1 = b - num10 * 10

c = a * num1
d = a * num10
e = a * num100

print(c)
print(d)
print(e)
print(c+10*d+100*e)