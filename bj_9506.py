import sys

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    else:
        list = [i for i in range(1, n) if n % i == 0]

        if n == sum(list):
            sys.stdout.write(str(n) + " = ")
            for i in range(len(list) - 1):
                sys.stdout.write(str(list[i]) + " + ")
            sys.stdout.write(str(list[len(list)-1]) + '\n')
        else:
            sys.stdout.write(str(n) + " is NOT perfect.\n")