# 예제 3-1 거스름돈 ) 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정. 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수 구하기

coin_list = [500, 100, 50, 10]

N = int(input())
count = 0

for coin in coin_list:
    count += N // coin
    N %= coin

print(count)