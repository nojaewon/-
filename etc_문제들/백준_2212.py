import sys
input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())

arr = list(map(int, input().rstrip().split()))
arr.sort()

if n <= k:
    print(0)
else:
    dist = []
    for i in range(1, n):
        dist.append(abs(arr[i-1] - arr[i]))
    dist.sort(reverse=True)
    total = sum(dist)
    for i in range(k-1):
        total -= dist[0]
        dist.pop(0)
    
    print(total)





