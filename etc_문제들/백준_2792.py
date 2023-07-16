import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for i in range(m):
    arr.append(int(input().rstrip()))

left, right = 1, max(arr)

while left < right:
    mid = (left + right) // 2
    
    person = 0
    for k in arr:
        person += k // mid
        remainder = k % mid

        
        if remainder > 0:
            person += 1
    
    if person > n:
        left = mid + 1
    else:
        right = mid

print(right)
        