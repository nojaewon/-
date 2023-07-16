import sys
input = sys.stdin.readline

H, W = map(int, input().split())
arr = list(map(int, input().split()))

total = 0

left = arr[0]
for i in range(1, W-1):
    if left <= arr[i]:
        left = arr[i]
        continue
    
    right = max(arr[i+1:])
    h = min(left, right)

    if h > arr[i]:
        total += h-arr[i]

print(total)
