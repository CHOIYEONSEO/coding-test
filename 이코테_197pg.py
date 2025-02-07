'''
정수 고유 번호의 부품 N개
M개 종류 부품 '대량' 구매
부품 M개 종류 '모두' 확인

있으면 yes, 없으면 no 출력
ie. no yes yes

1 <= N <= 1,000,000
1 <= M <= 100,000
-> 이진 탐색
'''
import sys
input = sys.stdin.readline

N = int(input())
have = list(map(int, input().rstrip().split()))
have.sort()

M = int(input())
want = list(map(int, input().rstrip().split()))

result = []
def binary_search(array, target, start, end):
    if start > end:
        return result.append('no')
    
    mid = (start + end) // 2

    if target == array[mid]:
        return result.append('yes')

    elif target > array[mid]:
        binary_search(array, target, mid + 1, end)

    else:
        binary_search(array, target, start, mid - 1)

for i in want:
    binary_search(have, i, 0, len(have))

print(" ".join(result))