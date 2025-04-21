import sys
import heapq
input = sys.stdin.readline

s = int(input().rstrip())
visited = [[False] * 1001 for _ in range(1001)] 
time = 0
display = 1
clipboard = 0

def bfs(time, display, clipboard):
  global s

  q = []
  heapq.heappush(q, (time, display, clipboard))
  
  while q:
    cur_time, cur_display, cur_clipboard = heapq.heappop(q)
    visited[cur_display][cur_clipboard] = True

    if cur_display == s:
      return cur_time

    for i in range(3):
      if i == 0:
        new_clipboard, new_display = cur_display, cur_display

      elif i == 1:
        new_clipboard, new_display = cur_clipboard, cur_clipboard + cur_display

      elif i == 2:
        new_clipboard, new_display = cur_clipboard, cur_display - 1

      if 0 <= new_clipboard < 1001 and 0 <= new_display < 1001 and not visited[new_display][new_clipboard]:
        visited[new_display][new_clipboard] = True
        heapq.heappush(q, (cur_time+1, new_display, new_clipboard))

print(bfs(time, display, clipboard))