import sys

list = [sys.stdin.readline().strip() for i in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(list[i]):
            sys.stdout.write(list[i][j])
            
sys.stdout.write('\n')