n = int(input())
list = []

for i in range(n):
    list.append(int(input()))

max = list[0]
num_l = 1
num_r = 1

for i in range(1, n):
    if list[i] > max:
        max = list[i]
        num_l += 1

list.reverse()

max = list[0]

for i in range(1, n):
    if list[i] > max:
        max = list[i]
        num_r += 1

print(num_l)
print(num_r)