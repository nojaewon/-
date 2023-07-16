import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []

for _ in range(n):
    a = int(input().rstrip())
    arr.append(a)

arr.sort()
max_value = arr[0] + k

start, end = arr[0], arr[0] + k

while start <= end:
    mid = (start + end) // 2
    tk = max_value - mid

    for i in range(1, n):
        if mid > arr[i]:
            tk -= (mid - arr[i])
        else:
            break
    
    if tk >= 0:
        start = mid + 1
    else:
        end = mid - 1

print(end)

