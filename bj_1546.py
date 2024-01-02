N = int(input())
list = list(map(int, input().split()))

max = list[0]
for i in range(1, N):
    if list[i] > max:
        max = list[i]

# 세준이의 새로운 성적 & 합 구하기
sum = 0 

for i in range(N):
    list[i] = list[i] / max * 100
    sum += list[i]

print(sum / N)