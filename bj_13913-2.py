from collections import deque
n, k = map(int, input().split())

visited = [False for _ in range(100001)]
time = 0
path = [n]

if n > k:
  print(n-k)

  for i in range(n, k-1, -1):
    print(i, end=" ")

else:
  q = deque([[time, n, path]])
  visited[n] = True

  while q:
    time, n, path = q.popleft()

    if n == k:
      print(time)
      print(" ".join(list(map(str, path))))
      break

    for i in range(3):
      if i == 0:
        nn = n - 1

      elif i == 1:
        nn = n + 1

      else:
        nn = 2 * n

      if 0 <= nn <= 100000 and not visited[nn]:
        visited[nn] = True

        q.append([time+1, nn, path+[nn]])