import sys

X, Y = sys.stdin.readline().split()

X = list(X)
X.reverse()
RevX = "".join(X)
Y = list(Y)
Y.reverse()
RevY = "".join(Y)

result1 = int(RevX) + int(RevY)

result1 = list(str(result1))
result1.reverse()

result = int("".join(result1))
print(result)