import sys, bisect
input = sys.stdin.readline

m = int(input().rstrip())

def target(k):
    result = 0
    while k > 0:
        result += k // 5
        k //= 5
    return result


start, end = 1, m*5

while start < end:
    mid = (start + end) // 2
    x = target(mid)

    if x < m:
        start = mid + 1
    else:
        end = mid

if target(end) == m:
    print(end)
else:
    print(-1)
