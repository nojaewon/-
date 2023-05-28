import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []

for i in range(n):
    arr.append(list(map(int ,sys.stdin.readline().rstrip().split())))

max_value = 0

for i in range(n):
    min_value = 10000
    for j in range(m):
        if min_value > arr[i][j]:
            min_value = arr[i][j]
    
    if max_value < min_value:
        max_value = min_value

print(max_value) 