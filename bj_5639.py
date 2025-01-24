'''
시간제한 : 1초
메모리제한 : 256mb

이진트리
전위 순휘 결과 -> 후위 순회 결과 출력

* 입력
트리를 전위 순회한 결과
노드에 들어있는 키의 값은 10^6보다 작은 양의 정수
노드의 수는 10,000개 이하

* 출력
후위 순회한 결과를 한 줄에 하나씩 출력
'''
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

pre = []
while True:
    try:
        pre.append(int(input().rstrip()))
    except:
        break

def post(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if pre[i] > pre[start]:
            mid = i
            break
    post(start + 1, mid - 1) #왼쪽 트리
    post(mid, end) #오른쪽 트리
    print(pre[start]) #루트 노드

post(0, len(pre) - 1)