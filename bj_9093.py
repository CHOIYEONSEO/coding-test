import sys

N = int(input())

for i in range(N):
    list1 = list(sys.stdin.readline().split())

    for j in range(len(list1)):
        list2 = list(list1[j])
        list2.reverse()
        sys.stdout.write(''.join(list2)+' ')
    sys.stdout.write('\n')