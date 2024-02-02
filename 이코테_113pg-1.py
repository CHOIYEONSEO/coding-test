N = int(input())

count = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if i // 10 == 3:
                count += 1
            elif i % 10 == 3:
                count += 1
            elif j // 10 == 3:
                count += 1
            elif j % 10 == 3:
                count += 1
            elif k // 10 == 3:
                count += 1
            elif k % 10 == 3:
                count += 1

print(count)