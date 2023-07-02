import sys
from collections import deque
input = sys.stdin.readline

A = []
N, L, R = map(int, input().split())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(N):
    temp = list(map(int, input().split()))
    A.append(temp)

def isIn(i, j):
    return i >= 0 and i < N and j >= 0 and j < N

def bfs(i, j, visited):        
    que=deque()
    guild=[]
    total = A[i][j]
    
    que.append((i, j))
    guild.append((i, j))
    visited[i][j] = True
    
    while que:
        y, x = que.popleft()
        
        for k in range(4):
            next_y = y + dy[k]
            next_x = x + dx[k]


            if isIn(next_y, next_x) and not visited[next_y][next_x]:
                dist = abs(A[y][x] - A[next_y][next_x])

                if L<=dist<=R:
                    que.append((next_y, next_x))
                    guild.append((next_y, next_x))
                    visited[next_y][next_x] = True
                    total += A[next_y][next_x]

    

    return total, guild

count = 0

while True:
    guild = []
    flag = 0
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                total, guild = bfs(i, j, visited)
                
                if len(guild) > 1:
                    flag = 1
                    total = total // len(guild)
                    for ty, tx in guild:
                        A[ty][tx] = total
    if flag == 0:
        break

    count += 1

print(count)
