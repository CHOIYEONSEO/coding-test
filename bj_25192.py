N = int(input())

record = []
for _ in range(N):
    record.append(input())

hello = []
result = 0

def countUnique(array = []):
    array = list(set(array))
    return len(array)

for i in range(N):
    if record[i] == 'ENTER':
        result += countUnique(hello)
        hello.clear()

    else:
        hello.append(record[i])

result += countUnique(hello)
print(result)