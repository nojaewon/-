import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

a = sorted(list(filter(lambda x: x > 0, arr[:])), reverse=True)
b = sorted(list(filter(lambda x: x < 0, arr[:])))

total = 0
for i in range(0, len(a), m):
    total += (2 * a[i])

for i in range(0, len(b), m):
    total += (2 * abs(b[i]))

if not a:
    total -= abs(b[0])
elif not b:
    total -= a[0]
else:
    total -= (a[0] if a[0] > abs(b[0]) else abs(b[0]))

print(total)



