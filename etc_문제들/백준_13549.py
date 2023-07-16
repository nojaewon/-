import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
que = deque()

min_cost = 100000
que.append((n, 0))
checked = [100000 for _ in range(100001)]

while que:
    value, cost = que.popleft()
    if value == k:
        min_cost = min(min_cost, cost)

    if value<0 or 100000<value:
        continue

    if checked[value] <= cost:
        continue
    
    checked[value] = cost

    que.append((value-1, cost+1))
    que.append((value+1, cost+1))
    que.append((value*2, cost))

print(min_cost)
