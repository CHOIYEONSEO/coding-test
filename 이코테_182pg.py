'''
A,B 배열. 두 배열 모두 N개의 자연수로 구성. (1 <= N <= 100,000)
최대 K번 바꿔치기 연산 : 배열 A 원소 하나 <-> 배열 B 원소 하나 (0 <= K <= N)
배열 A 모든 원소의 합이 최대가 되도록

최대 K번의 바꿔치기 연산을 수행해 만들 수 있는 배열 A의 모든 원소 합의 최댓값 출력
-> "라이브러리 정렬 후"(놓친 포인트) A의 가장 작은 숫자를 B의 가장 큰 숫자와 swap
'''
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

for i in range(K):
    if A[i] < B[len(B)-1-i]:
        A[i], B[len(B)-1-i] = B[len(B)-1-i], A[i]
    else:
        break

print(sum(A))