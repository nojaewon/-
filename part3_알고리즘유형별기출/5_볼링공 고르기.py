from collections import Counter
import sys
8
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

counter = Counter(arr)

c1 = n * (n-1) // 2
c2 = 0

for item in counter.items():
    if item[1] > 1:
        c2 += (item[1] * (item[1]-1)) // 2

print(c1 - c2)

