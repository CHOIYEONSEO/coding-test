'''
* n : 항상 10의 배수
* 500원, 100원, 50원, 10원 동전
'''
import sys
input = sys.stdin.readline

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)