import sys
from collections import deque
input = sys.stdin.readline

que = deque()
direction = [(0, 1), (1, 1), (1, 0)]

arr = []
N = int(input().rstrip())
for i in range(N):
    arr.append(list(map(int, input().split())))

p = []
for i in range(N):
    q = []
    for j in range(N):
        q.append([0, 0, 0])
    p.append(q)


p[0][1][0] = 1
for i in range(N):
    for j in range(2, N):
        #p[a][b][k]는 (a,b)에서 k번째 유형으로 끝나는 경우의 경로의 개수

        # 0, 2 유형인 경우는 (i,j)가 벽이 아니여야 함
        if arr[i][j] != 1:
            p[i][j][0] = p[i][j-1][0] + p[i][j-1][1]
            
            if i > 0:
                p[i][j][2] = p[i-1][j][1] + p[i-1][j][2]

        # 1 유형인 경우는 (i,j), (i-1,j), (i,j-1)이 벽이 아니여야 함 
        if arr[i][j] !=1 and arr[i-1][j] != 1 and arr[i][j-1] != 1:
            p[i][j][1] = p[i-1][j-1][0] + p[i-1][j-1][1] + p[i-1][j-1][2]

print(sum(p[N-1][N-1][:]))
                
