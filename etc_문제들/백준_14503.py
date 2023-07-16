import sys
input = sys.stdin.readline


n, m = map(int, input().split())
y, x, direction = map(int, input().split())

cleaned = [[0]*m for _ in range(n)]
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

count = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while True:
    flag = 0
    if cleaned[y][x] == 0:
        count += 1
        cleaned[y][x] = 1
    
    for k in range(1, 5):
        d = (direction + k*3) % 4
        nx = dx[d] + x
        ny = dy[d] + y
        if 0<=ny<n and 0<=nx<m and arr[ny][nx]==0 and cleaned[ny][nx]==0:
            y, x = ny, nx
            direction = d
            flag = 1
            break
    
    if flag==0:
        ny, nx = y + dy[(direction+2)%4], x + dx[(direction+2)%4]
        
        if arr[ny][nx]==1:
            break
        else:
            y, x = ny, nx

print(count)












