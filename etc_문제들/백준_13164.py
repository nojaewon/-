import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
dist = []

for i in range(1, n):
    dist.append(abs(arr[i-1] - arr[i]))

dist.sort()

for i in range(k-1):
    dist.pop()

print(sum(dist))