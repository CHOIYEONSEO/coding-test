import sys

while True:
    X = input()

    if X == '0':
        break
    else:
        temp = 1
        for i in range(len(X)//2 + 1):
            if X[i] == X[len(X)-i-1] and temp == 1:
                temp = 1
            elif X[i] != X[len(X)-i-1]:
                temp = 0
                break

        if temp == 1:
            sys.stdout.write("yes\n")
        else:
            sys.stdout.write("no\n")