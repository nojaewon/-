import sys
from collections import deque

arr = []
que = deque()

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

n, m = map(int, sys.stdin.readline().rstrip().split())
for i in range(n):
    arr.append(list(map(int, list(sys.stdin.readline().rstrip()))))

arr[0][0] = 2
que.append((0, 0))

while que:
    y, x = que.popleft()

    if y == n-1 and x == m-1:
        break
    
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]

        if ty < 0 or tx < 0 or ty >= n or tx >= m:
            continue
        
        if arr[ty][tx] == 1:
            arr[ty][tx] = arr[y][x] + 1
            que.append((ty, tx))

print(arr[n-1][m-1]-1)