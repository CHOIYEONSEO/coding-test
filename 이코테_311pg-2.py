n = int(input())
num = list(map(int, input().split()))

num.sort()

result = 0
count = 0
for i in num:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)