import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())

arr = [[0] * m for _ in range(n)]


for _ in range(k):
    ly, lx, ry, rx = list(map(int, input().split()))
    for i in range(ly, ry):
        for j in range(lx, rx):
            arr[i][j] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j):
    que = deque()
    count = 1
    arr[i][j] = 1
    que.append((i, j))

    while que:
        ty, tx = que.popleft()

        for k in range(4):
            ny = ty + dy[k]
            nx = tx + dx[k]

            if 0<=ny<n and 0<=nx<m and arr[ny][nx] == 0:
                arr[ny][nx] = 1
                count += 1
                que.append((ny, nx))
    return count

count = 0
temp = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            count += 1
            temp.append(bfs(i ,j))

temp.sort()

print(count)
for t in temp:
    print(t, end=" ")