A, B, V = map(int, input().split())

h = 0
if ((h + A) >= V):
    result = 1
    print(result)
else:
    V = V - A

    h = A - B
    if (V % h) == 0:
        result = 1 + V // h
    else:
        result = 2 + V // h
    print(result)
