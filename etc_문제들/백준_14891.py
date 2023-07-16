import sys
import copy
from collections import deque
input = sys.stdin.readline

p = []

for i in range(4):
    q = deque(map(int, list(input().rstrip())))
    p.append(q)

k = int(input().rstrip())
for _ in range(k):
    n, r = map(int, input().split())
    left, right = -1, 4
    for i in range(n-2, -1, -1):
        if p[i][2] == p[i+1][6]:
            left = i
            break
    
    for i in range(n, 4):
        if p[i-1][2] == p[i][6]:
            right = i
            break

    tr = copy.deepcopy(r) * -1
    for i in range(n-1, left, -1):
        p[i].rotate(r)
        r *= -1

    
    for i in range(n, right):
        p[i].rotate(tr)
        tr *= -1

total = 0
for idx, i in enumerate([1, 2, 4, 8]):
    total += p[idx][0] * i

print(total)
