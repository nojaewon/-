import sys

arr = []
n, m = map(int, sys.stdin.readline().rstrip().split())

d = []

def dfs(i, j):
    if i<0 or j<0 or i>=n or j>=m:
        return
    
    if arr[i][j] == 1:
        return
    
    arr[i][j] = 1

    dfs(i-1, j)
    dfs(i+1, j)
    dfs(i, j-1)
    dfs(i, j+1)
    

for i in range(n):
    arr.append(list(map(int, list(sys.stdin.readline().rstrip()))))

count = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            count += 1
            dfs(i, j)

print(count)
